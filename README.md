# 🛏️ Sleep Disorder Prediction using Health & Lifestyle Data

This project predicts whether a person suffers from **Insomnia**, **Sleep Apnea**, or **No Sleep Disorder** using health and lifestyle attributes via a machine learning model deployed as a Streamlit web app.

🌐 **Live App:**  
[https://sanskar-sdp.streamlit.app](https://sanskar-sdp.streamlit.app)

---

## 🚀 About the Project

This end-to-end project demonstrates how to build and deploy a predictive health model using real-world-style data. It integrates **data cleaning, feature engineering, machine learning**, and **deployment** on Streamlit Cloud.

Built as part of my applied machine learning portfolio.

---

## 🧠 Machine Learning Pipeline (In Detail)

### 🔹 1. Dataset

- Source: [Sleep Health and Lifestyle Dataset]
- Format: `.xlsx`, 400 records, 13 columns
- Target variable: `Sleep Disorder` with classes:
  - `None`
  - `Insomnia`
  - `Sleep Apnea`

---

### 🔹 2. Data Cleaning & Preprocessing

| Task                      | Method Used                                  |
|---------------------------|-----------------------------------------------|
| Drop ID column            | `Person ID` removed as it provides no value   |
| Handle missing values     | Filled missing `Sleep Disorder` with `"None"` |
| Feature transformation    | Split `Blood Pressure` into systolic/diastolic |
| Text normalization        | Standardized `"Normal Weight"` → `"Normal"`  |
| Label Encoding            | Categorical columns encoded using `LabelEncoder` (`sklearn`) |

---

### 🔹 3. Handling Class Imbalance

Original class distribution:

Insomnia 219
Sleep Apnea 78
None 77


To avoid prediction bias:
- Used **`resample()`** from `sklearn.utils` to **upsample** minority classes
- Ensured **equal class representation** in the training dataset

---

### 🔹 4. Model Selection & Training

| Step              | Details                                      |
|-------------------|----------------------------------------------|
| Algorithm         | `RandomForestClassifier` (ensemble model)    |
| Library           | `scikit-learn`                               |
| Splitting         | `train_test_split` with 30% test data        |
| Evaluation        | Accuracy, class balance, real-time prediction |
| Storage           | Model saved using `joblib` for reuse         |

✅ Model trained on **balanced data** for generalization across all sleep disorder types.

---

### 🔹 5. Deployment Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| **Streamlit** | Frontend UI and interaction     |
| **joblib**    | Model and label encoder loading |
| **GitHub**    | Version control + public repo   |
| **Streamlit Cloud** | One-click deployment      |

---

## 📊 Features Used for Prediction

- Gender
- Age
- Occupation
- Sleep Duration (hrs)
- Quality of Sleep (1–10)
- Physical Activity Level
- Stress Level (1–10)
- BMI Category
- Heart Rate (bpm)
- Daily Steps
- Systolic BP
- Diastolic BP

---

## 📁 File Structure

| File                                 | Description                                      |
|--------------------------------------|--------------------------------------------------|
| `app.py`                             | Streamlit app code                               |
| `sleep_disorder_model.pkl`           | Trained model file                               |
| `feature_columns.pkl`                | List of features used during training            |
| `label_encoder.pkl`                  | LabelEncoder to decode predictions               |
| `requirements.txt`                   | Python libraries to install                      |
| `Sleep_health_and_lifestyle_dataset.xlsx` | Source dataset (400 records)              |
| `Sleeping_Disorder_Prediction.ipynb` | Training notebook for model development          |
| `AppfeatureModel.ipynb`              | App integration / input testing notebook         |

---

## 🧪 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Sanskar1303/Sleep-Disorder-Prediction-by-Sanskar-Gajbhiye.git
cd Sleep-Disorder-Prediction-by-Sanskar-Gajbhiye

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
