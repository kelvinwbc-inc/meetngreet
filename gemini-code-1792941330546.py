import requests

class HKOClient:
    """Client for retrieving weather data from Hong Kong Observatory Open Data API."""
    
    BASE_URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"

    def __init__(self, lang="tc"):
        """
        :param lang: Language code ('tc' for Traditional Chinese, 'sc' for Simplified Chinese, 'en' for English)
        """
        self.lang = lang

    def get_current_weather(self):
        """Fetch current weather report including temperature, humidity, and warnings."""
        params = {"dataType": "rwd", "lang": self.lang}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_weather_forecast(self):
        """Fetch 9-day weather forecast."""
        params = {"dataType": "fnd", "lang": self.lang}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_weather_warnings(self):
        """Fetch summary of weather warnings currently in force."""
        params = {"dataType": "warnsum", "lang": self.lang}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()