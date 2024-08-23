import sys
import requests
import json

def parse_Arguments():
    import argparse
    parser = argparse.ArgumentParser(description="retrieve weather data for a specified city or country, or both")
    parser.add_argument("place", help="specify the location as 'city-country' (example: Asuncion-PY)")
    parser.add_argument("--output", choices=['json', 'csv', 'plain'], default='plain', help="choose the format for the output")
    return parser.parse_args()
