
import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Dashboard")

# Dummy data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
calories = np.random.randint(1500, 3000, size=7)

df = pd.DataFrame({
    "Day": days,
    "Calories": calories
})

st.line_chart(df.set_index("Day"))

st.success("Weekly Progress Displayed ✅")
