
# 🤖 Autonomous Skill-Based Tool-Calling Agent

An intelligent, modular ReAct AI agent deployed on Streamlit Cloud. Built with **LangGraph** and powered by **Mistral AI**, this agent dynamically routes user requests to specialized local and external skills (live web search, real-time weather updates, and safe mathematical computation).

---

## 🚀 Live Demo

Access the hosted application here:  
👉 **[Live Streamlit App](https://tool-calling-agent-5cgnuhafkdl2munkctttaj.streamlit.app/)**

---

## ✨ Features & Active Skills

- **🌐 Live Web Search (`search_web`)**: Powered by Tavily API to fetch current events, news, sports results, and live facts without date hallucinations.
- **🌤️ Real-Time Weather (`get_weather_info`)**: Fetches accurate, location-specific live weather and temperature forecasts via `wttr.in`.
- **🧮 Safe Math Execution (`calculate`)**: Evaluates mathematical expressions using standard Python mathematical modules safely.
- **⚡ Modern LangGraph Engine**: Built on LangGraph's ReAct state engine with cached agent runtime to minimize CPU overhead.
- **📅 Dynamic Date Context**: Injects precise date awareness into the conversation state to ensure queries always target accurate temporal context.

---

## 🛠️ Architecture & Tech Stack

- **Frontend / UI**: Streamlit
- **Agent Framework**: LangChain, LangGraph (`langgraph.prebuilt`)
- **LLM Engine**: Mistral AI (`langchain-mistralai`)
- **Search Tooling**: Tavily Search API
- **Deployment Platform**: Streamlit Cloud

---

## 🔑 Required API Credentials

To run the application locally or on Streamlit Cloud, you will need:

1. **Mistral API Key**: Get your key from [Mistral AI Console](https://console.mistral.ai/).
2. **Tavily API Key**: Get your key from [Tavily AI](https://tavily.com/).

You can enter these keys directly in the sidebar interface or save them in Streamlit secrets (`.streamlit/secrets.toml`):

```toml
MISTRAL_API_KEY = "your_mistral_api_key_here"
TAVILY_API_KEY = "your_tavily_api_key_here"

📂 Project Structure
tool-calling-agent/
├── app.py                 # Streamlit chat interface & runtime orchestration
├── requirements.txt       # Production dependencies
├── core/
│   ├── agent_engine.py    # LangGraph ReAct agent builder
│   └── skill_registry.py  # Unified registry aggregating modular agent skills
└── skills/
    ├── web_search.py      # Tavily search integration
    ├── weather_service.py # Live weather API integration
    └── math_solver.py     # Safe math evaluator tool

⚙️ Local Development Setup
 * Clone the repository:
   git clone [https://github.com/YOUR_USERNAME/tool-calling-agent.git](https://github.com/YOUR_USERNAME/tool-calling-agent.git)
cd tool-calling-agent

 * Install dependencies:
   pip install -r requirements.txt

 * Launch the Streamlit app:
   streamlit run app.py


