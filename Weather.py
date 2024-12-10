import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Predefined OpenWeather API Key (replace this with your actual API key)
API_KEY = "a2a61255349a253782218ede53c8596d"  # Replace with your actual API key

# Function to fetch weather data from OpenWeather API
def fetch_weather_data(city, api_key=API_KEY):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to plot weather data using Plotly
def plot_weather_data(data, city):
    df = pd.DataFrame({
        "Parameter": ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"],
        "Value": [data["main"]["temp"], data["main"]["humidity"], data["main"]["pressure"]]
    })
    

# Streamlit Dashboard
st.title("🌦️ Weather")
st.write("Get real-time weather updates for your favorite cities!")
st.write("Hello Please check the city name ")

# Input field for City
city = st.text_input("Enter the name of a city:")

# Fetch and display weather data
if city:
    st.write(f"Today's Weather")
    data = fetch_weather_data(city)
    if data:
        # Display weather metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperature (°C)", f"{data['main']['temp']} °C")
        col2.metric("💧 Humidity (%)", f"{data['main']['humidity']} %")
        col3.metric("📏 Pressure (hPa)", f"{data['main']['pressure']} hPa")

    else:
        st.error("❌ Failed to fetch weather data. Please check the city name.")
