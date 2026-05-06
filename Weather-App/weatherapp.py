import requests
city = input("Enter your city :")
api_key = ("28f94e8d4ec2bc4bd6270ba7f6ebb971")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
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




