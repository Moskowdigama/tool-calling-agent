from skills.web_search import search_web
from skills.math_solver import calculate
from skills.weather_service import get_weather_info

def get_all_skills():
    """Returns a unified list of registered tool skills available to the agent."""
    return [
        search_web,
        calculate,
        get_weather_info
    ]
