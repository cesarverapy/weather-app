import os
from typing import Optional
from dotenv import load_dotenv

class Config:
    """Configuration class for the weather application."""
    
    def __init__(self):
        load_dotenv()
        self.api_key: Optional[str] = os.getenv("OPENWEATHER_API_KEY")
        self.base_url: str = "http://api.openweathermap.org/data/2.5/weather"
        self.units: str = "metric"
        
    def validate(self) -> bool:
        """Validate the configuration."""
        if not self.api_key:
            return False
        return True 