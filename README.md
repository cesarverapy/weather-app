# WeatherApp

This CLI application fetches and displays weather data for a given location (city and country). It uses the OpenWeatherMap API to retrieve the data and can display the output in plain text, JSON, or CSV formats.

## Requirements

- Python 3.6+
- `requests` library
- `python-dotenv` library for environment variable handling

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

   ```bash
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage

Run the script with the following command:

```bash
python weather_tool.py Asuncion-PY --output json
```

- Replace `Asuncion-PY` with your desired location.
- Use the `--output` flag to choose the format (`json`, `csv`, or `plain`).

## Testing

To run the unit tests, use:

```bash
python -m unittest discover tests
```

---

## Future Improvements

- Add Frontend

---

Enjoy using the WeatherApp! ☀️🌦️
