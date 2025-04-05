import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.write('Simple Data Dashboard')

upload_file = st.file_uploader("Choose a CSV File",type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    
    st.subheader('Data Preview')
    st.write(df.head())
    
    st.subheader('Data Summary')
    st.write(df.describe())
    
    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Selected Column to filter by", columns)
    unique_values = df(selected_columns).unique()
    selected_value = st.selectbox("Selected Value", unique_values)
    
    filter_df = df[df[selected_columns] == selected_value]
    st.write(filter_df)
    
    st.subheader('Plot Data')
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filter_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting for file upload...")
        
    
    