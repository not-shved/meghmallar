import requests


print("Welcome to Megh-Mallar")
print("A CLImate Application")

city = input("Enter City name: ")
CITY = city
data = ""

with open("keys/openweather.txt", 'r') as file:
    API_KEY = file.readline().strip()


URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url=URL)

if response.status_code == 200:
    data = response.json()

print("Weather: ", data["weather"][0]["main"])
print("Temperature: ", data["main"]["temp"])

