# checker/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

# 1. Front-end page render krne ke liye view
def index_page(request):
    return render(request, 'index.html')


# 2. Main API View jo status check kre ga
class CheckWhatsAppNumber(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        
        # Validation: Agar input khali hai
        if not phone_number:
            return Response(
                {"error": "Please enter a phone number."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Safai: Number se saare extra spaces ya alphabets khatam krna
        clean_number = "".join(filter(str.isdigit, str(phone_number)))
        
        # Smart Country Code Fixer: Agar user ne local zero se start kiya (e.g., 0300...)
        if clean_number.startswith("0") and len(clean_number) == 11:
            clean_number = "92" + clean_number[1:]
        
        # Length check
        if len(clean_number) < 10 or len(clean_number) > 15:
            return Response({
                "status": "success",
                "is_available": False,
                "message": "Invalid number length"
            }, status=status.HTTP_200_OK)

        # ---- REAL THIRD-PARTY WHAPI INTEGRATION (OFFICIAL CHECK METHOD) ----
        # Whapi ka actual status checker endpoint URL query parameter ke sath yeh hai:
        API_URL = f"https://gate.whapi.cloud/contacts/{clean_number}"
        API_TOKEN = "ZKUlWzXWXp1pU2in5jFTAHBo6BODdTdr"
        
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Accept": "application/json"
        }
        
        try:
            # Sahi endpoint ke liye GET request jati hai, koi body request nahi chahiye hoti
            response = requests.get(API_URL, headers=headers, timeout=10)
            
            print("\n" + "="*50)
            print(f"DEBUG: Checking Number -> {clean_number}")
            print(f"DEBUG: Whapi Status Code -> {response.status_code}")
            print(f"DEBUG: Whapi Raw Response -> {response.text}")
            print("="*50 + "\n")
            
            # Whapi response status 200 tab deta hai jab contact mil jaye ya accurate information ho
            if response.status_code == 200:
                api_data = response.json()
                
                # Agar response mein error nahi hai aur valid data majood hai
                # Whapi direct contact object return krta hai jismein status ya profile hoti hai
                if "error" not in api_data:
                    return Response({
                        "status": "success",
                        "is_available": True,
                        "message": "Available on WhatsApp"
                    }, status=status.HTTP_200_OK)
            
            # Agar error code 404 aaye ya status valid na ho, to number whatsapp par nahi hai
            return Response({
                "status": "success",
                "is_available": False,
                "message": "Not available on WhatsApp"
            }, status=status.HTTP_200_OK)
            
        except requests.exceptions.RequestException as e:
            print(f"\nDEBUG: API EXCEPTION OCCURRED -> {e}\n")
            return Response({
                "status": "success",
                "is_available": False,
                "message": "Server Connection Error"
            }, status=status.HTTP_200_OK)