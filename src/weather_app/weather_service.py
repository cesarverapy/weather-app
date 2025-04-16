import requests
from typing import Dict, Optional
from .config import Config
from .exceptions import WeatherServiceError

class WeatherService:
    """Service class for interacting with the weather API."""
    
    def __init__(self, config: Config):
        self.config = config
        if not config.validate():
            raise WeatherServiceError("Invalid configuration: API key is missing")
            
    def get_weather(self, city: str, country: str) -> Dict:
        """Fetch weather data for a given location."""
        try:
            params = {
                'q': f"{city},{country}",
                'appid': self.config.api_key,
                'units': self.config.units
            }
            
            response = requests.get(self.config.base_url, params=params)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise WeatherServiceError(f"Failed to fetch weather data: {str(e)}")
            
    def format_weather_data(self, data: Dict) -> Dict:
        """Format the raw weather data into a more usable structure."""
        try:
            return {
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
        except KeyError as e:
            raise WeatherServiceError(f"Invalid weather data format: {str(e)}") 