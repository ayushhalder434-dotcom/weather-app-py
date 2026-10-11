import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Weather & Wardrobe Assistant", page_icon="🌤️")

st.title("🌤️ Weather & Wardrobe Assistant")
st.write("Enter a city to check current weather and get outfit suggestions!")

# City input
city = st.text_input("Enter City Name", "Mumbai")

# Public demo API key
API_KEY = "66f7939b69a170c52b8dc93b229ada99"

if st.button("Check Weather"):
    if city.strip():
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description'].capitalize()
            humidity = data['main']['humidity']
            
            # Display metrics
            col1, col2 = st.columns(2)
            col1.metric("Temperature", f"{temp} °C")
            col2.metric("Condition", weather_desc)
            st.write(f"**Humidity:** {humidity}%")
            
            # Outfit recommendation logic
            st.subheader("💡 Wardrobe Recommendation:")
            if temp < 10:
                st.warning("🧥 **Cold:** Wear a heavy coat, scarf, and warm layers!")
            elif 10 <= temp <= 22:
                st.info("🧥 **Mild:** A light jacket, sweater, or hoodie works best.")
            else:
                st.success("👕 **Warm:** Wear a light t-shirt and comfortable shorts or trousers.")
                
            if "rain" in weather_desc.lower():
                st.error("☔ **Rain Alert:** Bring an umbrella or a raincoat!")
        else:
            st.error("City not found. Please check spelling.")
    else:
        st.warning("Please type a city name first.")