"""
import pickle
import gradio as gr

# تحميل النموذج
model = pickle.load(open('diabetes_model.pkl', 'rb'))

# دالة التنبؤ
def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness,
                     insulin, bmi, dpf, age):
    data = [[pregnancies, glucose, blood_pressure, skin_thickness,
             insulin, bmi, dpf, age]]
    result = model.predict(data)
    if result[0] == 1:
        return "⚠️ Diabetes is detected. Hope you get well soon..."
    else:
        return "✅ Alhamdollelah, Diabetes is not found..."

# واجهة Gradio
interface = gr.Interface(
    fn=predict_diabetes,
    inputs=[
        gr.Number(label="Pregnancies"),
        gr.Number(label="Glucose"),
        gr.Number(label="BloodPressure"),
        gr.Number(label="SkinThickness"),
        gr.Number(label="Insulin"),
        gr.Number(label="BMI"),
        gr.Number(label="DiabetesPedigreeFunction"),
        gr.Number(label="Age")
    ],
    outputs="text",
    title="Diabetes Predictor",
    description="ادخل بياناتك لتحديد احتمالية الإصابة بالسكري"
)

interface.launch()
"""

import streamlit as st
import pickle
import numpy as np

# عنوان التطبيق
st.title("Diabetes Predictor")
st.write("ادخل البيانات التالية لمعرفة احتمالية الإصابة بالسكري:")

# تحميل نموذج التنبؤ
@st.cache_resource
def load_model():
    with open('diabetes_model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# مدخلات البيانات
pregnancies = st.number_input("Pregnancies", min_value=0, value=1)
glucose = st.number_input("Glucose", min_value=0, value=100)
blood_pressure = st.number_input("BloodPressure", min_value=0, value=70)
skin_thickness = st.number_input("SkinThickness", min_value=0, value=20)
insulin = st.number_input("Insulin", min_value=0, value=79)
bmi = st.number_input("BMI", min_value=0.0, value=25.0)
dpf = st.number_input("DiabetesPedigreeFunction", min_value=0.0, value=0.5)
age = st.number_input("Age", min_value=0, value=30)

# زر التنبؤ
if st.button("Predict"):
    data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    result = model.predict(data)
    
    if result[0] == 1:
        st.error("⚠️ Diabetes is detected. Hope you get well soon...")
    else:
        st.success("✅ Alhamdollelah, Diabetes is not found...")