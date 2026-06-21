from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import studentdata
from .serializers import studentserializers

class studentviews(APIView):
    def get(self, request):
        studentrecord=studentdata.objects.all()
        serializer=studentserializers(studentrecord,many=True)

        return Response(serializer.data)
    def post(self,request):
        serializer=studentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
  
class studentdelete(APIView):  
    def delete(self,request,pk):
        try:
          student=studentdata.objects.get(pk=pk)
          student.delete()
          return Response('student deleted!',status=status.HTTP_204_NO_CONTENT)
        except student.DoesNotExist:
            return Response('student not exist!',status=status.HTTP_404_NOT_FOUND)

class studentupdate(APIView):
    def put(self,request,pk):
        try: 
            student=studentdata.objects.get(pk=pk)
            studentserializer=studentserializers(student,data=request.data)
            if studentserializer.is_valid():
                studentserializer.save()
                return Response(studentserializer.data,status=status.HTTP_200_OK)
            return Response(studentserializer.data,status=status.HTTP_400_BAD_REQUEST)
        except studentdata.DoesNotExist:
          return Response('student not exist!', status=status.HTTP_404_NOT_FOUND)

# Create your views here.