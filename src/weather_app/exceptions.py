class WeatherAppError(Exception):
    """Base exception for the weather application."""
    pass

class WeatherServiceError(WeatherAppError):
    """Exception raised for weather service related errors."""
    pass

class ConfigurationError(WeatherAppError):
    """Exception raised for configuration related errors."""
    pass 