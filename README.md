# Dietary-Calories-Aanlysis-
AI-Based Dietary Calorie Analysis System - 4th Sem DL Project
# 🥗 AI-Based Dietary Calorie Analysis System

> Smart food tracking for Indian students using Deep Learning

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## 🎯 What This Project Does
A deep learning system for Indian students (age 15–30) that:
- 📸 Recognizes food from photos
- 🔢 Estimates calories automatically
- 📊 Tracks daily & weekly food habits
- 💡 Gives personalized diet recommendations
- 🧮 Calculates BMI & daily calorie needs

---
<!--
## 👨‍💻 Team
| Member | Role | Module |
|--------|------|--------|
| M1 (Dixa08) | DL Lead | Food Recognition - MobileNetV2 |
| M2 | Health Analytics | BMI / BMR / Calorie Prediction |
| M3 | Recommendation | Pattern Detection + Alerts |
| M4 | Dashboard + Auth | Streamlit UI + Face Login |
-->
---

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Language | Python 3.10 |
| Deep Learning | TensorFlow / Keras |
| Frontend | Streamlit |
| Image Processing | OpenCV + PIL |
| Face Auth | face_recognition |
| Database | SQLite + CSV |
| Visualization | Plotly + Matplotlib |

---

## 📁 Project Structure
```
Dietary-Calories-Analysis/
├── app.py              # Main Streamlit app
├── config.py           # Global settings
├── src/                # All modules
├── pages/              # Streamlit pages
├── database/           # SQLite + CSV files
├── models/             # Trained DL models
├── notebooks/          # Training notebooks
└── dataset/            # Food images
```

---

## ⚙️ Setup
```bash
git clone https://github.com/Dixa08/Dietary-Calories-Aanlysis-.git
cd Dietary-Calories-Aanlysis-
pip install -r requirements.txt
python database/init_db.py
streamlit run app.py
```

---

## 📊 Models Used
- 🔵 CNN Baseline (custom)
- 🟣 MobileNetV2 (transfer learning)
- 🟢 MLP Regression (calorie prediction)
- 🟠 LSTM (eating pattern detection)

---

*4th Semester Deep Learning Project — 2026*
