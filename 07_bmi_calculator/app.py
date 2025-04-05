import streamlit as st
import pandas as pd

st.title("BMI Calculator.")

height = st.slider("Enter your height (in cm) :",100,250,175)
weight = st.slider("Enter your weight (in kg) :",40,150,70)

bmi = weight / ((height/100)**2)
st.success(f"Your Boddy Mass Index is {bmi:.2f}.")

st.write("### BMI Categories: ###")
st.write(" - UnderWeight: BMI less than 18.5")  
st.write(" - NormalWeight: BMI between 18.5 and 24.9")
st.write(" - OverWeight: BMI between 25 and 29.9")
st.write(" - Obesity: BMI 30 or above")

st.write("Made with 🤍 by Muhammad Hammad ur Rehman")
