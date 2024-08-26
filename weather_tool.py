import sys
import requests
import json

def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser(description="retrieve weather data for a specified city or country, or both")
    parser.add_argument("place", help="specify the location as 'city-country' (example: Asuncion-PY)")
    parser.add_argument("--output", choices=['json', 'csv', 'plain'], default='plain', help="choose the format for the output")
    return parser.parse_args()

def fetch_weather_data(city_name, country_code, api_key):
    endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"
    try:
        result = requests.get(endpoint)
        result.raise_for_status()
        return result.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"Other error occurred: {err}")
    
    return None

def display_data(weather_info, format_type):
    if format_type == 'json':
        print(json.dumps(weather_info, indent=2))

    elif format_type == 'csv':
        temperature = weather_info['main']['temp']
        description = weather_info['weather'][0]['description']
        print(f"temperature,{temperature} \ncondition, {description}")
    
    else:
        temperature = weather_info['main']['temp']
        description = weather_info['weather'][0]['description']
        print(f"the current temperature is {temperature} ºC with {description}")

def main():
    args = parse_arguments()
    try:
        city, country = args.place.split('-')
    except ValueError:
        print("error: please ensure the location is in the format 'city-country'. example: Asuncion-PY ")
        sys.exit(1)

    api_key = "d099d30e2a258e30c80fff3ba41f044e"
    weather_info = fetch_weather_data(city, country, api_key)

    if weather_info:
        display_data(weather_info, args.output)


if __name__ == "__main__":
    main()