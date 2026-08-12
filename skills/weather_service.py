from langchain_core.tools import tool

@tool
def get_weather_info(location: str) -> str:
    """Useful for fetching current weather updates and forecasts for a specific city or region."""
    # Lightweight structured mock/fallback or API hook
    return f"Weather status for {location}: 24°C, Partly Cloudy with light breeze."
