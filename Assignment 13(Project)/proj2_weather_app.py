import json
import urllib.request
import urllib.parse

def get_weather(city_name):
    print("Fetching weather data...")
    try:
        # Using wttr.in JSON API format - open and free without API keys
        url = f"https://wttr.in/{urllib.parse.quote(city_name)}?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            temp_c = data['current_condition'][0]['temp_C']
            condition = data['current_condition'][0]['weatherDesc'][0]['value']
            feels_like = data['current_condition'][0]['FeelsLikeC']
            
            print(f"\nWeather in {city_name}:")
            print(f"Condition: {condition}")
            print(f"Temperature: {temp_c}°C (Feels like {feels_like}°C)")
            
    except Exception as e:
        print(f"Could not fetch weather data for '{city_name}'.")
        print(f"Error details: {e}")
        print("Note: Ensure you are connected to the internet.")

def main():
    print("--- Simple Weather App ---")
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            break
        if city:
            get_weather(city)

if __name__ == "__main__":
    main()
