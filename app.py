import streamlit as st
import joblib


model = joblib.load("bearing_model.pkl")


st.title("AI Based Bearing Fault Prediction")


rpm = st.number_input("RPM")

temperature = st.number_input("Temperature °C")

vibration = st.number_input("Vibration")

load = st.number_input("Load")


if st.button("Predict"):

    result = model.predict(
        [[rpm, temperature, vibration, load]]
    )

    if result[0] == 1:
        st.error("⚠ Bearing Fault Detected")
    else:
        st.success("✅ Bearing Healthy")
