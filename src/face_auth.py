import face_recognition
import numpy as np
import cv2
import sqlite3
import pickle

DB_PATH = "database/users.db"

def get_db():
    return sqlite3.connect(DB_PATH)

def encode_face(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_encodings(rgb)

    if len(faces) == 0:
        return None
    return faces[0]

def save_face(username, encoding):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users SET face_encoding=? WHERE username=?
    """, (pickle.dumps(encoding), username))

    conn.commit()
    conn.close()

def get_all_faces():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT username, face_encoding FROM users")
    data = cursor.fetchall()
    conn.close()

    users = []
    encodings = []

    for username, enc in data:
        if enc:
            users.append(username)
            encodings.append(pickle.loads(enc))

    return users, encodings

def recognize_face(image):
    encoding = encode_face(image)
    if encoding is None:
        return None

    users, encodings = get_all_faces()

    if len(encodings) == 0:
        return None

    matches = face_recognition.compare_faces(encodings, encoding)
    
    for i, match in enumerate(matches):
        if match:
            return users[i]

    return None
