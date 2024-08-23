import sys
import requests
import json

def parse_Arguments():
    import argparse
    parser = argparse.ArgumentParser(description="retrieve weather data for a specified city or country, or both")
    parser.add_argument("place", help="specify the location as 'city-country' (example: Asuncion-PY)")
    parser.add_argument("--output", choices=['json', 'csv', 'plain'], default='plain', help="choose the format for the output")
    return parser.parse_args()

def fetch_weather_Data(city_name, country_code, api_key):
    endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}, {country_code}, {api_key} & units = metric"
    try:
        result = requests.get(endpoint)
        result.raise_for_status()
        return result.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"Other error occurred: {err}")
    
    return None
