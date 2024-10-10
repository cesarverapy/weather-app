import unittest
from weather_tool import fetch_weather_data, display_data
from unittest.mock import patch

class TestWeatherTool(unittest.TestCase):

    @patch('weather_tool.requests.get')
    def test_fetch_weather_data_success(self, mock_get):
        # Mock successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 25, 'humidity': 60},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 3.5}
        }
        data = fetch_weather_data('Asuncion', 'PY', 'dummy_api_key')
        self.assertIsNotNone(data)
        self.assertEqual(data['main']['temp'], 25)

    @patch('weather_tool.requests.get')
    def test_fetch_weather_data_failure(self, mock_get):
        # Mock failure response
        mock_get.return_value.status_code = 404
        data = fetch_weather_data('UnknownCity', 'UnknownCountry', 'dummy_api_key')
        self.assertIsNone(data)

    def test_display_data_plain_format(self):
        # Test display_data with plain format
        weather_info = {
            'main': {'temp': 25, 'humidity': 60},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 3.5}
        }
        display_data(weather_info, 'plain')

    def test_display_data_csv_format(self):
        # Test display_data with CSV format
        weather_info = {
            'main': {'temp': 25, 'humidity': 60},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 3.5}
        }
        display_data(weather_info, 'csv')

if __name__ == '__main__':
    unittest.main()
