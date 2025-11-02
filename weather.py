import requests

API_KEY = "https://wttr.in"

def get_weather(city):
    url = f"{API_KEY}/{city}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        print("Weather:", response.text)
    else:
        print("Error fetching weather")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
import requests

API_KEY = "https://wttr.in/"

city = input("Enter city name: ")

res = requests.get(f"{API_KEY}{city}?format=3")

print(res.text)
