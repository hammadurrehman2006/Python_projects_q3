import streamlit as st

# Title
st.markdown("<h1 style='text-align: center;'>Unit Converter</h1>", unsafe_allow_html=True)
# User input for quanity selection

unit = st.selectbox("Choose a unit", [
    "Length", "Mass", "Time", "Temperature", "Speed",
    "Volume", "Area", "Pressure", "Energy", "Power",
    "Data Size", "Data Transfer Rate", "Angle", "Frequency"
])

# Length Conversion
if unit == "Length":
    measurement = st.number_input("Enter the measurement in meters", value=0.0)
    conversion_options = [
        "Meters to Kilometers", "Meters to Centimeters", "Meters to Millimeters",
        "Meters to Inches", "Meters to Feet", "Meters to Yards", "Meters to Miles"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Meters to Kilometers":
        result = measurement / 1000
        st.success(f"{measurement} meters is equal to {result:.1f} kilometers.")
    elif selected_conversion == "Meters to Centimeters":
        result = measurement * 100
        st.success(f"{measurement} meters is equal to {result:.1f} centimeters.")
    elif selected_conversion == "Meters to Millimeters":
        result = measurement * 1000
        st.success(f"{measurement} meters is equal to {result:.1f} millimeters.")
    elif selected_conversion == "Meters to Inches":
        result = measurement * 39.3701
        st.success(f"{measurement} meters is equal to {result:.1f} inches.")
    elif selected_conversion == "Meters to Feet":
        result = measurement * 3.28084
        st.success(f"{measurement} meters is equal to {result:.1f} feet.")
    elif selected_conversion == "Meters to Yards":
        result = measurement * 1.09361
        st.success(f"{measurement} meters is equal to {result:.1f} yards.")
    elif selected_conversion == "Meters to Miles":
        result = measurement / 1609.34
        st.success(f"{measurement} meters is equal to {result:.5f} miles.")

# Mass Conversion
elif unit == "Mass":
    measurement = st.number_input("Enter the measurement in kilograms", value=0.0)
    conversion_options = [
        "Kilograms to Grams", "Kilograms to Milligrams", "Kilograms to Pounds",
        "Kilograms to Ounces", "Kilograms to Tons"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Kilograms to Grams":
        result = measurement * 1000
        st.success(f"{measurement} kilograms is equal to {result:.1f} grams.")
    elif selected_conversion == "Kilograms to Milligrams":
        result = measurement * 1_000_000
        st.success(f"{measurement} kilograms is equal to {result:.1f} milligrams.")
    elif selected_conversion == "Kilograms to Pounds":
        result = measurement * 2.20462
        st.success(f"{measurement} kilograms is equal to {result:.1f} pounds.")
    elif selected_conversion == "Kilograms to Ounces":
        result = measurement * 35.274
        st.success(f"{measurement} kilograms is equal to {result:.1f} ounces.")
    elif selected_conversion == "Kilograms to Tons":
        result = measurement / 1000
        st.success(f"{measurement} kilograms is equal to {result:.5f} tons.")

# Time Conversion
elif unit == "Time":
    measurement = st.number_input("Enter the measurement in seconds", value=0.0)
    conversion_options = [
        "Seconds to Minutes", "Seconds to Hours", "Seconds to Days",
        "Seconds to Weeks", "Seconds to Years"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Seconds to Minutes":
        result = measurement / 60
        st.success(f"{measurement} seconds is equal to {result:.1f} minutes.")
    elif selected_conversion == "Seconds to Hours":
        result = measurement / 3600
        st.success(f"{measurement} seconds is equal to {result:.5f} hours.")
    elif selected_conversion == "Seconds to Days":
        result = measurement / 86400
        st.success(f"{measurement} seconds is equal to {result:.5f} days.")
    elif selected_conversion == "Seconds to Weeks":
        result = measurement / 604800
        st.success(f"{measurement} seconds is equal to {result:.5f} weeks.")
    elif selected_conversion == "Seconds to Years":
        result = measurement / 31536000
        st.success(f"{measurement} seconds is equal to {result:.5f} years.")

# Temperature Conversion
elif unit == "Temperature":
    measurement = st.number_input("Enter the temperature in Celsius", value=0.0)
    conversion_options = [
        "Celsius to Fahrenheit", "Celsius to Kelvin"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Celsius to Fahrenheit":
        result = (measurement * 9/5) + 32
        st.success(f"{measurement}°C is equal to {result:.1f}°F.")
    elif selected_conversion == "Celsius to Kelvin":
        result = measurement + 273.15
        st.success(f"{measurement}°C is equal to {result:.1f} K.")

# Speed Conversion
elif unit == "Speed":
    measurement = st.number_input("Enter the speed in meters per second", value=0.0)
    conversion_options = [
        "Meters/Second to Kilometers/Hour", "Meters/Second to Miles/Hour",
        "Meters/Second to Feet/Second"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Meters/Second to Kilometers/Hour":
        result = measurement * 3.6
        st.success(f"{measurement} m/s is equal to {result:.1f} km/h.")
    elif selected_conversion == "Meters/Second to Miles/Hour":
        result = measurement * 2.23694
        st.success(f"{measurement} m/s is equal to {result:.1f} mph.")
    elif selected_conversion == "Meters/Second to Feet/Second":
        result = measurement * 3.28084
        st.success(f"{measurement} m/s is equal to {result:.1f} ft/s.")

# Volume Conversion
elif unit == "Volume":
    measurement = st.number_input("Enter the volume in liters", value=0.0)
    conversion_options = [
        "Liters to Milliliters", "Liters to Cubic Meters", "Liters to Gallons",
        "Liters to Ounces"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Liters to Milliliters":
        result = measurement * 1000
        st.success(f"{measurement} liters is equal to {result:.1f} milliliters.")
    elif selected_conversion == "Liters to Cubic Meters":
        result = measurement / 1000
        st.success(f"{measurement} liters is equal to {result:.5f} cubic meters.")
    elif selected_conversion == "Liters to Gallons":
        result = measurement * 0.264172
        st.success(f"{measurement} liters is equal to {result:.1f} gallons.")
    elif selected_conversion == "Liters to Ounces":
        result = measurement * 33.814
        st.success(f"{measurement} liters is equal to {result:.1f} ounces.")

# Area Conversion
elif unit == "Area":
    measurement = st.number_input("Enter the area in square meters", value=0.0)
    conversion_options = [
        "Square Meters to Square Kilometers", "Square Meters to Square Feet",
        "Square Meters to Acres", "Square Meters to Hectares"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Square Meters to Square Kilometers":
        result = measurement / 1_000_000
        st.success(f"{measurement} square meters is equal to {result:.5f} square kilometers.")
    elif selected_conversion == "Square Meters to Square Feet":
        result = measurement * 10.7639
        st.success(f"{measurement} square meters is equal to {result:.1f} square feet.")
    elif selected_conversion == "Square Meters to Acres":
        result = measurement / 4046.86
        st.success(f"{measurement} square meters is equal to {result:.5f} acres.")
    elif selected_conversion == "Square Meters to Hectares":
        result = measurement / 10_000
        st.success(f"{measurement} square meters is equal to {result:.5f} hectares.")

# Pressure Conversion
elif unit == "Pressure":
    measurement = st.number_input("Enter the pressure in Pascals", value=0.0)
    conversion_options = [
        "Pascals to Kilopascals", "Pascals to Atmospheres", "Pascals to Bars",
        "Pascals to PSI"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Pascals to Kilopascals":
        result = measurement / 1000
        st.success(f"{measurement} Pascals is equal to {result:.1f} kilopascals.")
    elif selected_conversion == "Pascals to Atmospheres":
        result = measurement / 101325
        st.success(f"{measurement} Pascals is equal to {result:.5f} atmospheres.")
    elif selected_conversion == "Pascals to Bars":
        result = measurement / 100000
        st.success(f"{measurement} Pascals is equal to {result:.5f} bars.")
    elif selected_conversion == "Pascals to PSI":
        result = measurement / 6894.76
        st.success(f"{measurement} Pascals is equal to {result:.5f} PSI.")

# Energy Conversion
elif unit == "Energy":
    measurement = st.number_input("Enter the energy in Joules", value=0.0)
    conversion_options = [
        "Joules to Kilojoules", "Joules to Calories", "Joules to Watt-Hours",
        "Joules to BTU"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Joules to Kilojoules":
        result = measurement / 1000
        st.success(f"{measurement} Joules is equal to {result:.1f} kilojoules.")
    elif selected_conversion == "Joules to Calories":
        result = measurement / 4.184
        st.success(f"{measurement} Joules is equal to {result:.1f} calories.")
    elif selected_conversion == "Joules to Watt-Hours":
        result = measurement / 3600
        st.success(f"{measurement} Joules is equal to {result:.5f} watt-hours.")
    elif selected_conversion == "Joules to BTU":
        result = measurement / 1055.06
        st.success(f"{measurement} Joules is equal to {result:.5f} BTU.")

# Power Conversion
elif unit == "Power":
    measurement = st.number_input("Enter the power in Watts", value=0.0)
    conversion_options = [
        "Watts to Kilowatts", "Watts to Horsepower", "Watts to BTU/Hour"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Watts to Kilowatts":
        result = measurement / 1000
        st.success(f"{measurement} Watts is equal to {result:.1f} kilowatts.")
    elif selected_conversion == "Watts to Horsepower":
        result = measurement / 746
        st.success(f"{measurement} Watts is equal to {result:.5f} horsepower.")
    elif selected_conversion == "Watts to BTU/Hour":
        result = measurement * 3.41214
        st.success(f"{measurement} Watts is equal to {result:.1f} BTU/hour.")

# Data Size Conversion
elif unit == "Data Size":
    measurement = st.number_input("Enter the data size in Bytes", value=0.0)
    conversion_options = [
        "Bytes to Kilobytes", "Bytes to Megabytes", "Bytes to Gigabytes",
        "Bytes to Terabytes"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Bytes to Kilobytes":
        result = measurement / 1024
        st.success(f"{measurement} Bytes is equal to {result:.1f} kilobytes.")
    elif selected_conversion == "Bytes to Megabytes":
        result = measurement / (1024 ** 2)
        st.success(f"{measurement} Bytes is equal to {result:.5f} megabytes.")
    elif selected_conversion == "Bytes to Gigabytes":
        result = measurement / (1024 ** 3)
        st.success(f"{measurement} Bytes is equal to {result:.5f} gigabytes.")
    elif selected_conversion == "Bytes to Terabytes":
        result = measurement / (1024 ** 4)
        st.success(f"{measurement} Bytes is equal to {result:.5f} terabytes.")

# Data Transfer Rate Conversion
elif unit == "Data Transfer Rate":
    measurement = st.number_input("Enter the transfer rate in Bits per Second", value=0.0)
    conversion_options = [
        "Bits/Second to Kilobits/Second", "Bits/Second to Megabits/Second",
        "Bits/Second to Gigabits/Second", "Bits/Second to Bytes/Second"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Bits/Second to Kilobits/Second":
        result = measurement / 1000
        st.success(f"{measurement} bits/second is equal to {result:.1f} kilobits/second.")
    elif selected_conversion == "Bits/Second to Megabits/Second":
        result = measurement / 1_000_000
        st.success(f"{measurement} bits/second is equal to {result:.5f} megabits/second.")
    elif selected_conversion == "Bits/Second to Gigabits/Second":
        result = measurement / 1_000_000_000
        st.success(f"{measurement} bits/second is equal to {result:.5f} gigabits/second.")
    elif selected_conversion == "Bits/Second to Bytes/Second":
        result = measurement / 8
        st.success(f"{measurement} bits/second is equal to {result:.1f} bytes/second.")

# Angle Conversion
elif unit == "Angle":
    measurement = st.number_input("Enter the angle in Degrees", value=0.0)
    conversion_options = [
        "Degrees to Radians", "Degrees to Gradians"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Degrees to Radians":
        result = measurement * (3.14159 / 180)
        st.success(f"{measurement} degrees is equal to {result:.5f} radians.")
    elif selected_conversion == "Degrees to Gradians":
        result = measurement * (10 / 9)
        st.success(f"{measurement} degrees is equal to {result:.1f} gradians.")

# Frequency Conversion
elif unit == "Frequency":
    measurement = st.number_input("Enter the frequency in Hertz", value=0.0)
    conversion_options = [
        "Hertz to Kilohertz", "Hertz to Megahertz", "Hertz to Gigahertz"
    ]
    selected_conversion = st.selectbox("Select a conversion", conversion_options)

    if selected_conversion == "Hertz to Kilohertz":
        result = measurement / 1000
        st.success(f"{measurement} Hz is equal to {result:.1f} kHz.")
    elif selected_conversion == "Hertz to Megahertz":
        result = measurement / 1_000_000
        st.success(f"{measurement} Hz is equal to {result:.5f} MHz.")
    elif selected_conversion == "Hertz to Gigahertz":
        result = measurement / 1_000_000_000
        st.success(f"{measurement} Hz is equal to {result:.5f} GHz.")