import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("housing_price_model.pkl")

# Page title
st.title("Sydney Housing Price Prediction")

st.write(
    "Enter the property details below to estimate the sale price."
)

# User inputs
suburb = st.selectbox(
    "Suburb",
    ["Beverly Hills", "Concord", "Castle Hill"]
)

property_type = st.selectbox(
    "Property Type",
    ["House", "Apartment", "Villa", "Semi-detached"]
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

# Engineered feature
total_rooms = bedrooms + bathrooms

# Prediction
if st.button("Predict Sale Price"):

    input_data = pd.DataFrame({
        "suburb": [suburb],
        "property_type": [property_type],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "total_rooms": [total_rooms]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Sale Price: ${prediction:,.0f}"
    )
