'''✅ 3. src/tracker.py
Weekly tracking + simple pattern detection
Python'''
import sqlite3

DB_PATH = "database/food_logs.db"

def get_weekly_summary(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, SUM(calories)
        FROM food_log
        WHERE user_id=?
        GROUP BY date
        ORDER BY date DESC
        LIMIT 7
    """, (user_id,))

    data = cursor.fetchall()
    conn.close()

    return data


def detect_pattern(weekly_data):
    if not weekly_data:
        return "No data available"

    calories = [day[1] for day in weekly_data]

    avg = sum(calories) / len(calories)

    if avg > 2500:
        return "High calorie intake trend ⚠️"
    elif avg < 1500:
        return "Low calorie intake ⚠️"
    else:
        return "Healthy eating pattern ✅"
