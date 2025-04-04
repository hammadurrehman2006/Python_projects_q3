import streamlit as st
import pandas as pd

st.title("BMI Calculator.")

height = st.slider("Enter your height (in cm) :",100,250,175)
weight = st.slider("Enter your weight (in kg) :",40,150,70)

bmi = weight / ((height/100)**2)
st.success(f"Your Boddy Mass Index is {bmi:.2f}.")