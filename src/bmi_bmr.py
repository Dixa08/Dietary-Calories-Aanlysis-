# src/bmi_bmr.py

import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model


# ---------------- BMI ----------------
def calculate_bmi(weight, height):
    height = height / 100
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category


# ---------------- BMR ----------------
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    return round(bmr, 2)


# ---------------- TDEE ----------------
def calculate_tdee(bmr, activity):
    activity_map = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }

    return round(bmr * activity_map.get(activity, 1.2), 2)


# ---------------- FOOD CALORIES ----------------
def get_food_calories(food_name):
    df = pd.read_csv("database/indian_food_calories.csv")

    if food_name in df["Food"].values:
        row = df[df["Food"] == food_name].iloc[0]

        return {
            "food": food_name,
            "calories": int(row["Calories"]),
            "protein": int(row["Protein"]),
            "carbs": int(row["Carbs"]),
            "fat": int(row["Fat"])
        }
    else:
        return None


# ---------------- ML PREDICTION ----------------
def predict_calories(age, weight, height, activity):
    try:
        model = load_model("models/calorie_mlp.keras")

        data = np.array([[age, weight, height, activity]])
        prediction = model.predict(data)

        return round(float(prediction[0][0]), 2)

    except:
        return None
