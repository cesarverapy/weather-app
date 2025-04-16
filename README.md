# WeatherApp

A command-line weather application that fetches and displays weather data for a given location. Built with clean architecture and SOLID principles.

## Features

- Fetch current weather data for any city and country
- Multiple output formats (JSON, CSV, plain text)
- Clean, modular code structure
- Type hints and proper error handling
- Easy to extend and maintain

## Requirements

- Python 3.6+
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/WeatherApp.git
   cd WeatherApp
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the OpenWeatherMap API key:
   Create a `.env` file with your API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage

Run the script with the following command:

```bash
python -m src.weather_app.main Asuncion-PY --output json
```

- Replace `Asuncion-PY` with your desired location
- Use the `--output` flag to choose the format (`json`, `csv`, or `plain`)

## Project Structure

```
src/
└── weather_app/
    ├── __init__.py
    ├── config.py         # Configuration management
    ├── display.py        # Output formatting
    ├── exceptions.py     # Custom exceptions
    ├── main.py          # Entry point
    └── weather_service.py # API interaction
```

## Future Improvements

- Add Frontend

---

Enjoy using the WeatherApp! ☀️🌦️
