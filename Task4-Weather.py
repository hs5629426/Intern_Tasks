import requests
import os

print("\t\t ------> WEATHER APP <--------\n")
SAVED_LOCATIONS = []

def get_weather_data(city_name):
    

    api_key = os.getenv('OPEN_WEATHER_API_KEY', '1e33ef117156191801d74c1f044a12fe')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code: {response.status_code}")


def get_forecast_data(city_name):
    
    api_key = os.getenv('3f9fb08d8072f76544cef185d70b63b1', '1e33ef117156191801d74c1f044a12fe')

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code: {response.status_code}")


def main():
    while True:
        print("\nSaved Locations:", SAVED_LOCATIONS)
        city_name = input("Enter the name of the city (or select from saved locations by index): ")

        # Allow users to select from saved locations
        if city_name.isdigit():
            city_name = SAVED_LOCATIONS[int(city_name)]

        try:
            weather_data = get_weather_data(city_name)
            forecast_data = get_forecast_data(city_name)

            # Display current weather data
            print("\nCurrent Weather:")
            print("---------------------\n")
            print(f"Temperature: {weather_data['main']['temp']}°Celsius")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
            print(f"Weather Conditions: {weather_data['weather'][0]['description']}")

            # Display forecast for the next two days
            print("\nTwo-Day Forecast:")
            print("---------------------")
            for i in range(0, 16, 8):  # API provides forecast for every 3 hours, so we'll skip 8 to get to the next day
                print(f"\nDate & Time: {forecast_data['list'][i]['dt_txt']}")
                print(f"Temperature: {forecast_data['list'][i]['main']['temp']}°C")
                print(f"Weather Conditions: {forecast_data['list'][i]['weather'][0]['description']}")

            # Option to save the location for quick access
            save_choice = input("\nDo you want to save this location for future reference? (y/n): ").lower()
            if save_choice == 'y' and city_name not in SAVED_LOCATIONS:
                SAVED_LOCATIONS.append(city_name)

        except Exception as e:
            print(str(e))

        # Ask user if they want to continue
        choice = input("\nDo you want to check another city's weather? Enter 'y' to continue or 'n' to exit: ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
