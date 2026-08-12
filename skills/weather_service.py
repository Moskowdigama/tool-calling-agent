import requests
from langchain_core.tools import tool

@tool
def get_weather_info(location: str) -> str:
    """Useful for fetching real-time weather updates and forecasts for a specific city or region."""
    try:
        url = f"https://wttr.in/{location}?format=%C+%t"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Current weather in {location}: {response.text.strip()}"
        return f"Could not fetch weather for {location}."
    except Exception as e:
        return f"Error retrieving weather: {str(e)}"
