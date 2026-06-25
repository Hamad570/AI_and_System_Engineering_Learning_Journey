import joblib
import numpy as np

# ===============================
# LOAD TRAINED MODELS
# ===============================
model_anxiety = joblib.load("model_anxiety.pkl")
model_level = joblib.load("model_level.pkl")
model_type = joblib.load("model_type.pkl")

# ===============================
# TEXT → NUMBER MAPPING
# ===============================
mapping = {
    "never": 0,
    "sometimes": 1,
    "often": 2,
    "always": 3,
    "yes": 3,
    "no": 0
}

# ===============================
# QUESTIONS (ORDER MUST MATCH TRAINING)
# ===============================
questions = [
    "Do you feel restless? (never/sometimes/often/always): ",
    "Do you feel increased heart rate? (never/sometimes/often/always): ",
    "Do you face breathing issues? (never/sometimes/often/always): ",
    "Do you have sleep issues? (never/sometimes/often/always): ",
    "Do you overthink frequently? (never/sometimes/often/always): ",
    "Do you fear about the future? (never/sometimes/often/always): ",
    "Do you face focus problems? (never/sometimes/often/always): ",
    "Do you feel work-related stress? (never/sometimes/often/always): ",
    "Do you have financial stress? (yes/no): ",
    "Do you feel nervous or uneasy? (never/sometimes/often/always): ",
    "Do you worry excessively about health? (never/sometimes/often/always): ",
    "Do you avoid social interaction? (never/sometimes/often/always): ",
    "Do you feel irritable often? (never/sometimes/often/always): ",
    "Do you experience panic attacks? (yes/no): "
]

# ===============================
# COLLECT USER INPUT
# ===============================
user_input = []

print("\nPlease answer the following questions honestly:\n")

for q in questions:
    ans = input(q).strip().lower()
    user_input.append(mapping.get(ans, 0))

X = np.array(user_input).reshape(1, -1)

# ===============================
# ADVICE LOGIC (RULE-BASED)
# ===============================
def get_advice(level, anxiety_type):
    advice = ""

    # Level-based guidance
    if level == "Low":
        advice += (
            "Low level anxiety detected.\n"
            "- Focus on maintaining a healthy routine.\n"
            "- Regular exercise and good sleep can prevent escalation.\n"
        )
    elif level == "Moderate":
        advice += (
            "Moderate level anxiety detected.\n"
            "- Stress management techniques are recommended.\n"
            "- Reduce triggers and prioritize mental well-being.\n"
        )
    else:
        advice += (
            "High level anxiety detected.\n"
            "- Professional mental health support is strongly recommended.\n"
            "- Do not ignore persistent or severe symptoms.\n"
        )

    # Type-based guidance
    if anxiety_type == "Financial":
        advice += (
            "\nFinancial Anxiety Guidance:\n"
            "- Create a simple budget and track expenses.\n"
            "- Focus on controllable financial actions.\n"
            "- Avoid constant worry about factors beyond control.\n"
        )
    elif anxiety_type == "Social":
        advice += (
            "\nSocial Anxiety Guidance:\n"
            "- Gradual exposure to social situations may help.\n"
            "- Work on self-confidence and communication skills.\n"
            "- Avoid complete isolation.\n"
        )
    elif anxiety_type == "Health":
        advice += (
            "\nHealth Anxiety Guidance:\n"
            "- Avoid excessive online symptom searching.\n"
            "- Trust qualified healthcare professionals.\n"
            "- Maintain a balanced health routine.\n"
        )
    elif anxiety_type == "Work":
        advice += (
            "\nWork-related Anxiety Guidance:\n"
            "- Set clear boundaries between work and personal life.\n"
            "- Take regular breaks and avoid burnout.\n"
            "- Discuss workload issues if possible.\n"
        )
    else:
        advice += (
            "\nGeneral Anxiety Guidance:\n"
            "- Practice mindfulness or relaxation techniques.\n"
            "- Maintain balanced daily routines.\n"
            "- Stay socially connected and physically active.\n"
        )

    return advice

# ===============================
# PREDICTION
# ===============================
has_anxiety = model_anxiety.predict(X)[0]

print("\n================= RESULT =================\n")

if has_anxiety == "No":
    print("No anxiety detected.")
    print(
        """You appear mentally healthy based on the provided inputs.
        You just overthink alot and focus more on body symptoms, in real
        you have No problem so don't worry and just focus on lifestyle\n"""
        "Advice:\n"
        "- Maintain a balanced lifestyle.\n"
        "- Get adequate sleep and exercise.\n"
        "- Manage daily stress proactively.\n"
    )
    print("""\nThis system is not a medical diagnostic tool.
       It is an anxiety pattern and risk detection model
       designed for academic experimentation.""")
else:
    level = model_level.predict(X)[0]
    anxiety_type = model_type.predict(X)[0]

    print("Anxiety Detected")
    print("Anxiety Level:", level)
    print("Anxiety Type:", anxiety_type)

    print("\nGuidance & Recommendations:")
    print(get_advice(level, anxiety_type))
print("""\nThis system is not a medical diagnostic tool.
       It is an anxiety pattern and risk detection model
       designed for academic experimentation.""")
print("==========================================\n")
