import argparse
import sys
from typing import Tuple

from .config import Config
from .weather_service import WeatherService
from .display import WeatherDisplay, OutputFormat
from .exceptions import WeatherAppError

def parse_arguments() -> Tuple[str, str, OutputFormat]:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Retrieve weather data for a specified city and country."
    )
    parser.add_argument(
        "place",
        help="Specify the location as 'city-country' (example: Asuncion-PY)"
    )
    parser.add_argument(
        "--output",
        choices=['json', 'csv', 'plain'],
        default='plain',
        help="Choose the format for the output."
    )
    args = parser.parse_args()
    
    try:
        city, country = args.place.split('-')
        return city, country, args.output
    except ValueError:
        raise WeatherAppError(
            "Invalid location format. Please use 'city-country' (example: Asuncion-PY)"
        )

def main() -> None:
    """Main entry point for the weather application."""
    try:
        city, country, output_format = parse_arguments()
        
        config = Config()
        if not config.validate():
            raise WeatherAppError("API key not found. Please set OPENWEATHER_API_KEY in .env file")
            
        service = WeatherService(config)
        weather_data = service.get_weather(city, country)
        formatted_data = service.format_weather_data(weather_data)
        
        WeatherDisplay.display(formatted_data, output_format)
        
    except WeatherAppError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 