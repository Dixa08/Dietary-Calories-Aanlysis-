
import streamlit as st
import cv2
from src.profile import login_user, register_user
from src.face_auth import encode_face, save_face, recognize_face

st.title("🔐 Login / Register")

menu = ["Login", "Register"]
choice = st.selectbox("Select Option", menu)

if choice == "Register":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if register_user(username, password):
            st.success("User Registered!")

            cap = cv2.VideoCapture(0)
            st.info("Capturing face...")

            ret, frame = cap.read()
            cap.release()

            encoding = encode_face(frame)
            if encoding is not None:
                save_face(username, encoding)
                st.success("Face Registered ✅")
            else:
                st.error("Face not detected")

        else:
            st.error("Username exists")

elif choice == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(username, password):
            st.success("Login Successful")

    if st.button("Login with Face"):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        user = recognize_face(frame)

        if user:
            st.success(f"Welcome {user}")
        else:
            st.error("Face not recognized")
