import sys
import requests
import argparse
import json
import os
import csv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Retrieve weather data for a specified city or country, or both.")
    parser.add_argument("place", help="Specify the location as 'city-country' (example: Asuncion-PY)")
    parser.add_argument("--output", choices=['json', 'csv', 'plain'], default='plain', help="Choose the format for the output.")
    return parser.parse_args()

def fetch_weather_data(city_name, country_code, api_key):
    endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"
    try:
        result = requests.get(endpoint)
        result.raise_for_status()  # Raise an exception for HTTP errors
        return result.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}") 
    except Exception as err:
        print(f"Unexpected error occurred: {err}")
    return None

def display_data(weather_info, format_type):
    try:
        temperature = weather_info['main'].get('temp', 'N/A')
        description = weather_info['weather'][0].get('description', 'N/A')
        humidity = weather_info['main'].get('humidity', 'N/A')
        wind_speed = weather_info['wind'].get('speed', 'N/A')

        if format_type == 'json':
            print(json.dumps(weather_info, indent=2))
        elif format_type == 'csv':
            # Using csv.writer to properly format CSV data
            writer = csv.writer(sys.stdout)
            writer.writerow(["temperature", "description", "humidity", "wind_speed"])
            writer.writerow([temperature, description, humidity, wind_speed])
        else:  # Plain text output
            print(f"The current temperature is {temperature}ºC with {description}.")
            print(f"Humidity: {humidity}% | Wind Speed: {wind_speed} m/s")
    except KeyError as e:
        print(f"Error: Missing data in the response - {e}")

def main():
    args = parse_arguments()

    try:
        city, country = args.place.split('-')
    except ValueError:
        print("Error: Please ensure the location is in the format 'city-country'. Example: Asuncion-PY.")
        sys.exit(1)

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: API key not found. Please set it in a .env file or environment variable.")
        sys.exit(1)

    weather_info = fetch_weather_data(city, country, api_key)

    if weather_info:
        display_data(weather_info, args.output)
    else:
        print("Error: Could not fetch weather data.")

if __name__ == "__main__":
    main()
