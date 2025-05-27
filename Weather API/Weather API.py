import requests
import json
from datetime import datetime

class WeatherClient:
    def __init__(self, api_key, units="metric"):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"
        self.units = units
        self.unit_symbols = {
            "metric": "°C",
            "imperial": "°F",
            "standard": "K"
        }

    def _make_request(self, endpoint, params):
        url = f"{self.base_url}{endpoint}"
        full_params = {
            "appid": self.api_key,
            "units": self.units,
            **params
        }
        response = requests.get(url, params=full_params)
        response.raise_for_status()
        return response.json()

    def get_current_weather(self, city_name=None, lat=None, lon=None):
        params = {}
        if city_name:
            params["q"] = city_name
        elif lat is not None and lon is not None:
            params["lat"] = lat
            params["lon"] = lon
        else:
            return None

        response = self._make_request("weather", params)
        if response:
            return self._parse_current_weather(response)
        return None

    def get_forecast_weather(self, city_name=None, lat=None, lon=None, num_days=5):
        params = {}
        if city_name:
            params["q"] = city_name
        elif lat is not None and lon is not None:
            params["lat"] = lat
            params["lon"] = lon
        else:
            return None

        response = self._make_request("forecast", params)
        if response:
            return self._parse_forecast_weather(response, num_days)
        return None

    def _parse_current_weather(self, data):
        try:
            city = data.get("name")
            country = data.get("sys", {}).get("country")
            temperature = data.get("main", {}).get("temp")
            feels_like = data.get("main", {}).get("feels_like")
            humidity = data.get("main", {}).get("humidity")
            pressure = data.get("main", {}).get("pressure")
            wind_speed = data.get("wind", {}).get("speed")
            weather_description = data.get("weather", [])[0].get("description") if data.get("weather") else "N/A"
            sunrise_ts = data.get("sys", {}).get("sunrise")
            sunset_ts = data.get("sys", {}).get("sunset")

            sunrise = datetime.fromtimestamp(sunrise_ts).strftime('%H:%M:%S') if sunrise_ts else 'N/A'
            sunset = datetime.fromtimestamp(sunset_ts).strftime('%H:%M:%S') if sunset_ts else 'N/A'

            return {
                "city": city,
                "country": country,
                "temperature": f"{temperature}{self.unit_symbols[self.units]}",
                "feels_like": f"{feels_like}{self.unit_symbols[self.units]}",
                "humidity": f"{humidity}%",
                "pressure": f"{pressure} hPa",
                "wind_speed": f"{wind_speed} m/s",
                "description": weather_description.capitalize(),
                "sunrise": sunrise,
                "sunset": sunset
            }
        except (KeyError, TypeError) as e:
            print(f"Error parsing current weather data: {e}")
            return None

    def _parse_forecast_weather(self, data, num_days):
        forecast_list = []
        if "list" in data:
            daily_forecasts = {}
            for item in data["list"]:
                dt_object = datetime.fromtimestamp(item["dt"])
                date_str = dt_object.strftime("%Y-%m-%d")
                if date_str not in daily_forecasts:
                    daily_forecasts[date_str] = []
                daily_forecasts[date_str].append(item)

            sorted_dates = sorted(daily_forecasts.keys())
            for i, date_str in enumerate(sorted_dates):
                if i >= num_days:
                    break

                day_data = daily_forecasts[date_str]
                selected_item = None
                for item in day_data:
                    dt_object = datetime.fromtimestamp(item["dt"])
                    if dt_object.hour >= 12 and dt_object.hour < 15:
                        selected_item = item
                        break
                if not selected_item and day_data:
                    selected_item = day_data[0]

                if selected_item:
                    try:
                        temperature = selected_item.get("main", {}).get("temp")
                        feels_like = selected_item.get("main", {}).get("feels_like")
                        humidity = selected_item.get("main", {}).get("humidity")
                        wind_speed = selected_item.get("wind", {}).get("speed")
                        weather_description = selected_item.get("weather", [])[0].get("description") if selected_item.get("weather") else "N/A"
                        forecast_list.append({
                            "date": date_str,
                            "time": datetime.fromtimestamp(selected_item["dt"]).strftime('%H:%M:%S'),
                            "temperature": f"{temperature}{self.unit_symbols[self.units]}",
                            "feels_like": f"{feels_like}{self.unit_symbols[self.units]}",
                            "humidity": f"{humidity}%",
                            "wind_speed": f"{wind_speed} m/s",
                            "description": weather_description.capitalize()
                        })
                    except (KeyError, TypeError) as e:
                        print(f"Error parsing forecast data for {date_str}: {e}")
                        continue
        return forecast_list

    def display_current_weather(self, city_name=None, lat=None, lon=None):
        print("\n--- Current Weather ---")
        weather_data = self.get_current_weather(city_name, lat, lon)
        if weather_data:
            print(f"Location: {weather_data['city']}, {weather_data['country']}")
            print(f"Temperature: {weather_data['temperature']} (Feels like: {weather_data['feels_like']})")
            print(f"Description: {weather_data['description']}")
            print(f"Humidity: {weather_data['humidity']}")
            print(f"Pressure: {weather_data['pressure']}")
            print(f"Wind Speed: {weather_data['wind_speed']}")
            print(f"Sunrise: {weather_data['sunrise']}")
            print(f"Sunset: {weather_data['sunset']}")
        else:
            print("Could not retrieve current weather data.")

    def display_forecast_weather(self, city_name=None, lat=None, lon=None, num_days=5):
        print(f"\n--- {num_days}-Day Forecast ---")
        forecast_data = self.get_forecast_weather(city_name, lat, lon, num_days)
        if forecast_data:
            current_date = None
            for forecast in forecast_data:
                if forecast["date"] != current_date:
                    print(f"\nDate: {forecast['date']}")
                    current_date = forecast["date"]
                print(f"  Time: {forecast['time']}")
                print(f"    Temperature: {forecast['temperature']} (Feels like: {forecast['feels_like']})")
                print(f"    Description: {forecast['description']}")
                print(f"    Humidity: {forecast['humidity']}")
                print(f"    Wind Speed: {forecast['wind_speed']}")
        else:
            print("Could not retrieve forecast weather data.")

if __name__ == "__main__":
    YOUR_API_KEY = 'your_actual_api_key_here'
       # While testing, this was my API key: '0d4b55c0ef79ba70fc5fe9a23978277f'
    if YOUR_API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("Please replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key.")
        print("You can get one from: https://openweathermap.org/api")
    else:
        weather_app = WeatherClient(YOUR_API_KEY, units="metric")

        while True:
            print("\n--- Weather Forecast Application ---")
            print("Choose an option:")
            print("1. Get weather by City Name")
            print("2. Get weather by Coordinates (Latitude & Longitude)")
            print("3. Exit")

            choice = input("Enter your choice (1, 2, or 3): ").strip()

            if choice == '1':
                city = input("Enter city name: ").strip()
                if city:
                    weather_app.display_current_weather(city_name=city)
                    forecast_choice = input("Do you want a 5-day forecast for this city? (yes/no): ").strip().lower()
                    if forecast_choice == 'yes':
                        weather_app.display_forecast_weather(city_name=city, num_days=5)
                else:
                    print("City name cannot be empty.")
            elif choice == '2':
                try:
                    lat = float(input("Enter Latitude: ").strip())
                    lon = float(input("Enter Longitude: ").strip())
                    weather_app.display_current_weather(lat=lat, lon=lon)
                    forecast_choice = input("Do you want a 5-day forecast for these coordinates? (yes/no): ").strip().lower()
                    if forecast_choice == 'yes':
                        weather_app.display_forecast_weather(lat=lat, lon=lon, num_days=5)
                except ValueError:
                    print("Invalid input. Latitude and Longitude must be numbers.")
            elif choice == '3':
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
