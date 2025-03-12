import streamlit as st   # python library: Streamlit

# Function to convert units
def convert_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }

    key = f"{unit_from}_{unit_to}" # generate a key on the input and output units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
st.title("Unit Converter ♻") # Web app title

value = st.number_input("Enter the value:", min_value= 1.0, step= 1.0)

unit_from = st.selectbox("Convert from:",["meters","kilometers","grams","kilograms"])

unit_to = st.selectbox("Convert to:", ["meters","kilometers","grams","kilograms"])

if st.button("convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Convert Value: {result}")

# Build by Abdul Wahid 