from langchain_core.tools import tool
import math

@tool
def calculate(expression: str) -> str:
    """Useful for evaluating mathematical expressions and complex calculations. Input must be a valid Python math expression string (e.g. '2 ** 8 + math.sin(0.5)')."""
    try:
        # Safe scope with math functions available
        allowed_globals = {"math": math, "abs": abs, "round": round, "pow": pow}
        result = eval(expression, {"__builtins__": None}, allowed_globals)
        return f"Calculation Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"
