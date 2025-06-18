# 🛏️ Sleep Disorder Prediction App

A machine learning-based web app that predicts whether a person has **Insomnia**, **Sleep Apnea**, or **No Sleep Disorder** based on lifestyle and health-related inputs.

🌐 **Live App:**  
[Click to Launch](https://sanskar1303-sleep-disorder-prediction-by-sanskar-gajbhiye.streamlit.app)

---

## 📁 Project Structure

| File                            | Description                                           |
|---------------------------------|-------------------------------------------------------|
| `app.py`                        | Streamlit web app for predictions                    |
| `AppfeatureModel.ipynb`         | Jupyter notebook for app integration/testing         |
| `Sleeping_Disorder_Prediction.ipynb` | Jupyter notebook for training the ML model         |
| `sleep_disorder_model.pkl`      | Trained Random Forest model                          |
| `feature_columns.pkl`           | List of features used during model training          |
| `label_encoder.pkl`             | LabelEncoder to decode predicted class labels        |
| `Sleep_health_and_lifestyle_dataset.xlsx` | Original dataset (400 records, 13 features)     |
| `requirements.txt`              | List of dependencies for deployment (rename needed)  |

---

## 🚀 Features

- Predicts sleep disorder based on inputs like age, sleep duration, activity level, stress, BP, etc.
- User-friendly web interface built with **Streamlit**
- Handles imbalanced classes using upsampling
- Deployable on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📊 Input Features

- Gender
- Age
- Occupation
- Sleep Duration
- Quality of Sleep (1–10)
- Physical Activity Level (0–100)
- Stress Level (1–10)
- BMI Category
- Heart Rate
- Daily Steps
- Systolic BP
- Diastolic BP

---

## 🧠 Model Used

- **Algorithm**: RandomForestClassifier (`sklearn`)
- **Preprocessing**:
  - Drop `Person ID`
  - Split `Blood Pressure` into systolic/diastolic
  - Label encode categorical columns
  - Balance dataset via resampling
- **Output**:
  - None
  - Insomnia
  - Sleep Apnea

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/Sanskar1303/Sleep-Disorder-Prediction-by-Sanskar-Gajbhiye.git
   cd Sleep-Disorder-Prediction-by-Sanskar-Gajbhiye
