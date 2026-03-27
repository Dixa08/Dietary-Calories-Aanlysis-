✅ 2. src/recommender.py
Gives goal-based suggestions
Python
def recommend_food(goal, consumed_calories, target_calories):
    
    remaining = target_calories - consumed_calories

    if goal == "weight_loss":
        if remaining > 300:
            return "You can eat a light meal like salad or fruits."
        else:
            return "Avoid more calories today. Drink water or green tea."

    elif goal == "muscle_gain":
        if remaining > 500:
            return "Add protein-rich food like eggs, paneer, or chicken."
        else:
            return "Good intake! Consider a protein shake."

    elif goal == "maintenance":
        if remaining > 200:
            return "Balanced meal recommended."
        else:
            return "You reached your daily calorie goal!"

    return "No recommendation available."
