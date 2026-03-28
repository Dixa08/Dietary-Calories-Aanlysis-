
# ============================================
# config.py - Global Settings for Whole Team
# ============================================

import os

# ── Project Paths ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset")
TRAIN_PATH   = os.path.join(DATASET_PATH, "train")
VAL_PATH     = os.path.join(DATASET_PATH, "val")
TEST_PATH    = os.path.join(DATASET_PATH, "test")
MODEL_PATH   = os.path.join(BASE_DIR, "models")
DB_PATH      = os.path.join(BASE_DIR, "database")

# ── Model Settings ──
IMAGE_SIZE    = (224, 224)
BATCH_SIZE    = 32
EPOCHS        = 15
NUM_CLASSES   = 10

# ── Food Classes ──
FOOD_CLASSES = [
    "biryani",
    "dal",
    "dosa",
    "idli",
    "paneer_curry",
    "poha",
    "rajma_chawal",
    "rice",
    "roti",
    "samosa"
]

# ── Diet Factors ──
ACTIVITY_FACTORS = {
    "sedentary":        1.2,
    "lightly_active":   1.375,
    "moderately_active":1.55,
    "very_active":      1.725
}

STRESS_ADJUSTMENT = {
    "low":    0,
    "medium": -100,
    "high":   -200
}

LIFESTYLE_ADJUSTMENT = {
    "healthy":  0,
    "moderate": -50,
    "unhealthy":-150
}

# ── Goal Settings ──
GOAL_ADJUSTMENT = {
    "lose":    -500,
    "gain":    +400,
    "maintain": 0
}

# ── Alert Thresholds ──
OVEREAT_THRESHOLD   = 1.15  # 15% above target
UNDEREAT_THRESHOLD  = 0.75  # 25% below target

# ── Database Files ──
USERS_DB    = os.path.join(DB_PATH, "users.db")
FOOD_LOG_DB = os.path.join(DB_PATH, "food_logs.db")
CALORIES_CSV= os.path.join(DB_PATH, "indian_food_calories.csv")
