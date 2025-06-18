import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load the trained model and feature list
# -----------------------------
model = joblib.load("sleep_disorder_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")  # List of column names used during training

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Sleep Disorder Prediction", layout="centered")
st.title("🛏️ Sleep Disorder Prediction App")
st.write("Fill in the details below to predict the likelihood of sleep disorders based on health and lifestyle metrics.")

# -----------------------------
# Input fields
# -----------------------------
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 80, 30)
occupation = st.selectbox("Occupation", [
    "Accountant", "Doctor", "Engineer", "Lawyer", "Manager", "Nurse", 
    "Sales Representative", "Salesperson", "Scientist", "Software Engineer", "Teacher"])
sleep_duration = st.slider("Sleep Duration (hrs)", 3.0, 12.0, 6.5)
quality_of_sleep = st.slider("Quality of Sleep (1–10)", 1, 10, 6)
physical_activity = st.slider("Physical Activity Level", 0, 100, 50)
stress_level = st.slider("Stress Level (1–10)", 1, 10, 5)
bmi_category = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
heart_rate = st.slider("Heart Rate (bpm)", 40, 120, 70)
daily_steps = st.slider("Daily Steps", 0, 20000, 5000)
systolic_bp = st.slider("Systolic BP", 80, 180, 120)
diastolic_bp = st.slider("Diastolic BP", 50, 120, 80)

# -----------------------------
# Manual encoding
# -----------------------------
gender_map = {"Male": 1, "Female": 0}
bmi_map = {"Underweight": 3, "Normal": 2, "Overweight": 1, "Obese": 0}  # Match your training encoding
occupation_list = [
    "Accountant", "Doctor", "Engineer", "Lawyer", "Manager", "Nurse", 
    "Sales Representative", "Salesperson", "Scientist", "Software Engineer", "Teacher"
]

input_dict = {
    "Gender": gender_map[gender],
    "Age": age,
    "Occupation": occupation_list.index(occupation),
    "Sleep Duration": sleep_duration,
    "Quality of Sleep": quality_of_sleep,
    "Physical Activity Level": physical_activity,
    "Stress Level": stress_level,
    "BMI Category": bmi_map[bmi_category],
    "Heart Rate": heart_rate,
    "Daily Steps": daily_steps,
    "systolic_bp": systolic_bp,
    "diastolic_bp": diastolic_bp
}

# Convert to DataFrame and reorder columns to match model training
input_data = pd.DataFrame([input_dict])[feature_cols]

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    label_map = {0: "None", 1: "Insomnia", 2: "Sleep Apnea"}  # Use the encoding from your model
    st.success(f"🧠 Predicted Sleep Disorder: **{label_map[prediction]}**")
