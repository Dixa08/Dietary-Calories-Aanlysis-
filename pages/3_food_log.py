✅ 1. src/food_logger.py
Handles storing and retrieving food logs (SQLite)
Python
import sqlite3
from datetime import datetime

DB_PATH = "database/food_logs.db"

def connect_db():
    return sqlite3.connect(DB_PATH)

def log_food(user_id, food_name, calories):
    conn = connect_db()
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO food_log (user_id, food_name, calories, date)
        VALUES (?, ?, ?, ?)
    """, (user_id, food_name, calories, date))

    conn.commit()
    conn.close()

    return "Food logged successfully!"

def get_daily_calories(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT SUM(calories) FROM food_log
        WHERE user_id=? AND date=?
    """, (user_id, date))

    result = cursor.fetchone()[0]
    conn.close()

    return result if result else 0

def get_food_history(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT food_name, calories, date
        FROM food_log
        WHERE user_id=?
        ORDER BY date DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return rows
