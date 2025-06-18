# 🛏️ Sleep Disorder Prediction using Lifestyle & Health Data

This project uses machine learning to predict the presence of a sleep disorder (Insomnia, Sleep Apnea, or None) based on a person’s lifestyle and medical metrics.

Deployed Live on **Streamlit Cloud**  
👉 [Click to Try the App](https://sanskar1303-sleep-disorder-prediction-by-sanskar-gajbhiye.streamlit.app)

---

## 🚀 About the Project

The goal is to develop an intelligent system that can predict sleep disorders using features like:
- Sleep duration
- Quality of sleep
- Stress level
- Heart rate
- Blood pressure
- Physical activity
- BMI category, and more.

We trained a **Random Forest Classifier** on a balanced version of the Sleep Health and Lifestyle dataset to improve prediction accuracy across all classes.

---

## 🧠 Model Workflow

1. **Data Preprocessing**
   - Removed non-informative ID fields
   - Handled missing values
   - Split blood pressure into systolic & diastolic
   - Encoded categorical variables

2. **Class Balancing**
   - The dataset was imbalanced (Insomnia dominated)
   - We used upsampling to balance all three classes

3. **Training**
   - Model: `RandomForestClassifier`
   - Library: `scikit-learn`
   - Evaluation: Accuracy, prediction diversity

4. **Deployment**
   - UI: `Streamlit`
   - Hosting: [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📊 Input Features Used

| Feature                  | Type      |
|--------------------------|-----------|
| Gender                   | Categorical |
| Age                      | Numeric   |
| Occupation               | Categorical |
| Sleep Duration           | Numeric (hours) |
| Quality of Sleep         | Rating (1–10) |
| Physical Activity Level  | Numeric |
| Stress Level             | Rating (1–10) |
| BMI Category             | Categorical |
| Heart Rate               | Numeric (bpm) |
| Daily Steps              | Numeric |
| Systolic BP              | Numeric |
| Diastolic BP             | Numeric |

---

## 🔍 Prediction Output

The model predicts one of the following:
- **None**
- **Insomnia**
- **Sleep Apnea**

---

## 📁 Files in this Repo

| File                      | Description |
|---------------------------|-------------|
| `app.py`                  | Streamlit web app source |
| `train_model.py`          | Model training script |
| `sleep_disorder_model.pkl`| Trained model file |
| `feature_columns.pkl`     | Saved feature names |
| `label_encoder.pkl`       | Encoder to decode model predictions |
| `requirements.txt`        | Dependencies for deployment |

---

## 🧪 Try It Yourself

```bash
git clone https://github.com/Sanskar1303/Sleep-Disorder-Prediction-by-Sanskar-Gajbhiye.git
cd Sleep-Disorder-Prediction-by-Sanskar-Gajbhiye
pip install -r requirements.txt
streamlit run app.py
