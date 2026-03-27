import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# ==============================
# CONFIG
# ==============================
MODEL_PATH = "models/mobilenetv2_food.keras"
LABELS_PATH = "models/label_classes.txt"
IMG_SIZE = 224

# ==============================
# LOAD MODEL & LABELS
# ==============================
model = load_model(MODEL_PATH)

def load_labels(label_path):
    with open(label_path, "r") as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

class_names = load_labels(LABELS_PATH)

# ==============================
# PREPROCESS IMAGE
# ==============================
def preprocess_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Invalid image format")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    img = img / 255.0  # normalize
    img = np.expand_dims(img, axis=0)

    return img

# ==============================
# PREDICT FUNCTION
# ==============================
def predict_food(image_path):
    try:
        img = preprocess_image(image_path)

        predictions = model.predict(img)
        predicted_index = np.argmax(predictions)
        confidence = float(np.max(predictions))

        food_name = class_names[predicted_index]

        return {
            "food": food_name,
            "confidence": round(confidence * 100, 2)
        }

    except Exception as e:
        return {
            "error": str(e)
        }

# ==============================
# TEST (RUN DIRECTLY)
# ==============================
if __name__ == "__main__":
    test_image = "sample.jpg"  # change path

    result = predict_food(test_image)

    if "error" in result:
        print("Error:", result["error"])
    else:
        print(f"Food: {result['food']}")
        print(f"Confidence: {result['confidence']}%")
