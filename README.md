
🤖 Modular Skill-Based Tool-Calling Agent
An autonomous AI agent built with LangGraph, Mistral AI, and Streamlit. Designed around a modular "Skill Registry" architecture, the agent dynamically decides when to query live web data, execute safe mathematical calculations, or fetch real-time global weather conditions.
🚀 Live Streamlit App: tool-calling-agent.streamlit.app
🌟 Key Features
 * Modular Skill Registry: Decoupled architecture allowing new tools/skills to be registered in isolation without altering core agent execution logic.
 * Real-Time Web Search: Integrates Tavily Search API for up-to-date factual retrieval and live news.
 * Live Weather Reports: Uses dynamic location querying via wttr.in for accurate, real-time meteorological status across any city or region.
 * Safe Mathematical Execution: Evaluates complex Python math expressions using a sandboxed evaluation engine.
 * Temporal Context Injection: Dynamic date and system prompt awareness to prevent AI date hallucinations.
 * Streamlit Web UI: Clean, responsive chat interface with state preservation and resource-cached agent invocation to keep memory and CPU overhead low.
🛠️ Project Structure
tool-calling-agent/
├── app.py                   # Main Streamlit web application & UI loop
├── requirements.txt         # Pinned Python package dependencies
├── core/
│   ├── agent_engine.py      # LangGraph ReAct agent builder & LLM configuration
│   └── skill_registry.py    # Aggregator registering modular skills for the agent
└── skills/
    ├── web_search.py        # Skill: Tavily web search integration
    ├── math_solver.py       # Skill: Safe Python math execution tool
    └── weather_service.py   # Skill: Live weather service tool

⚙️ Active Modular Skills
| Skill Name | Purpose | Underlying Service |
|---|---|---|
| search_web | Searches the live internet for recent facts, news, and current events. | Tavily Search API |
| calculate | Evaluates mathematical equations and complex functions (math.sin, pow, etc.). | Custom Python Engine |
| get_weather_info | Fetches live weather updates and forecasts for any location. | wttr.in API |
🚀 Local Setup & Installation
Prerequisites
 * Python 3.10+
 * Mistral AI API Key
 * Tavily API Key
Steps
 * Clone the repository:
   git clone https://github.com/YOUR_USERNAME/tool-calling-agent.git
cd tool-calling-agent

 * Install dependencies:
   pip install -r requirements.txt

 * Set up Environment Variables (Optional):
   Create a .env file in the root directory:
   MISTRAL_API_KEY=your_mistral_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

 * Run the Streamlit application:
   streamlit run app.py

🔑 Deployment Credentials
When running on Streamlit Cloud, provide your keys either in the app sidebar or under Settings → Secrets:
MISTRAL_API_KEY = "your_mistral_key"
TAVILY_API_KEY = "your_tavily_key"

🧰 Tech Stack
 * Framework: LangChain / LangGraph
 * LLM Engine: Mistral AI (mistral-small-latest)
 * Web Interface: Streamlit
 * Search Backend: Tavily AI
 
