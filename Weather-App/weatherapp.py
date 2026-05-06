import requests
city = input("Enter your city :")
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
if response.status_code ==200:
 data = response.json()
 print("\nWeather Details:\n")
 print("📍City:", city)
 print("☁🌡️Temp:", data["main"]["temp"])
 print("☁️Weather:", data["weather"][0]["description"])
 print("💧Humidity:", data["main"]["humidity"])
else:
    print("Error: Check City Name Or API.")




