import streamlit as st
import pandas as pd

# Load CSV dataset
file_path = r'C:\Users\nandh\OneDrive\Desktop\crop recommendation  project\Crop_recommendation.csv'
df = pd.read_csv(file_path)  # Read the CSV file

# Function to find the best matching crop recommendation
def recommend_crop(N, P, K, Temperature, Humidity, ph, Rainfall):
    try:
        # Convert user inputs to float
        N, P, K, Temperature, Humidity, ph, Rainfall = map(float, [N, P, K, Temperature, Humidity, ph, Rainfall])

        # Find the closest match in the dataset (Simple Filtering, Can be Improved)
        match = df[
            (df["N"] == N) &
            (df["P"] == P) &
            (df["K"] == K) &
            (df["Temperature"] == Temperature) &
            (df["Humidity"] == Humidity) &
            (df["ph"] == ph) &
            (df["Rainfall"] == Rainfall)
        ]

        if not match.empty:
            return match["Crop"].values[0]  # Assuming the crop column is named "Crop"
        else:
            return "No exact match found. Try adjusting input values."
    except ValueError:
        return "Invalid Input! Please enter numerical values."

# Streamlit App UI
def main():
    st.title('🌱 Crop Recommendation System')

    # Background image
    st.image("https://media.sciencephoto.com/image/c0236973/800wm/C0236973-Ripe_cotton_crop.jpg", use_column_width=True)

    # Input fields
    N = st.text_input("Nitrogen (N)", "")
    P = st.text_input("Phosphorus (P)", "")
    K = st.text_input("Potassium (K)", "")
    Temperature = st.text_input("Temperature (°C)", "")
    Humidity = st.text_input("Humidity (%)", "")
    ph = st.text_input("pH Level", "")
    Rainfall = st.text_input("Rainfall (mm)", "")

    result = ""

    # Predict button
    if st.button("Predict Crop"):
        result = recommend_crop(N, P, K, Temperature, Humidity, ph, Rainfall)
        st.success(f"🌾 Recommended Crop: {result}")
        st.toast(f"Recommended Crop: {result}")

    if st.button("About"):
        st.info("📌 **Data-Driven Crop Recommendation**")
        st.write("This system recommends crops based on soil nutrient levels (N, P, K), temperature, humidity, pH, and rainfall.")

# Run the app
if __name__ == "__main__":
    main()
