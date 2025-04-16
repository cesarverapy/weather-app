import json
import csv
import sys
from typing import Dict, Literal

OutputFormat = Literal['json', 'csv', 'plain']

class WeatherDisplay:
    """Class for displaying weather data in different formats."""
    
    @staticmethod
    def display(weather_data: Dict, format_type: OutputFormat = 'plain') -> None:
        """Display weather data in the specified format."""
        if format_type == 'json':
            print(json.dumps(weather_data, indent=2))
        elif format_type == 'csv':
            writer = csv.writer(sys.stdout)
            writer.writerow(weather_data.keys())
            writer.writerow(weather_data.values())
        else:  # plain text
            print(f"Current Weather:")
            print(f"Temperature: {weather_data['temperature']}°C")
            print(f"Description: {weather_data['description']}")
            print(f"Humidity: {weather_data['humidity']}%")
            print(f"Wind Speed: {weather_data['wind_speed']} m/s") 