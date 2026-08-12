import os
import streamlit as st
from langchain_core.messages import HumanMessage
from core.agent_engine import build_agent_executor

st.set_page_config(page_title="Skill-Based Tool-Calling Agent", page_icon="🤖", layout="wide")

st.title("🤖 Autonomous Skill-Based Tool-Calling Agent")
st.markdown("An intelligent ReAct agent leveraging modular skills for web search, math, and live weather calculations.")

mistral_key = st.secrets.get("MISTRAL_API_KEY") if "MISTRAL_API_KEY" in st.secrets else None
tavily_key = st.secrets.get("TAVILY_API_KEY") if "TAVILY_API_KEY" in st.secrets else None

with st.sidebar:
    st.header("🔑 API Credentials")
    if not mistral_key:
        mistral_key = st.text_input("Mistral API Key", type="password")
    if not tavily_key:
        tavily_key = st.text_input("Tavily API Key", type="password")
    
    st.markdown("---")
    st.markdown("**Active Modular Skills:**")
    st.markdown("- 🌐 `search_web`: Live search via Tavily")
    st.markdown("- 🧮 `calculate`: Safe Python math execution")
    st.markdown("- 🌤️ `get_weather_info`: Live weather reports")

if mistral_key and tavily_key:
    os.environ["TAVILY_API_KEY"] = tavily_key
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me to search the web, calculate math, or check weather..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking & calling skills..."):
                agent = build_agent_executor(mistral_key)
                
                response = agent.invoke({"messages": [HumanMessage(content=prompt)]})
                
                output_text = response["messages"][-1].content
                
                st.markdown(output_text)
                st.session_state.messages.append({"role": "assistant", "content": output_text})
else:
    st.warning("Please provide both your Mistral API Key and Tavily API Key in the sidebar to activate the agent.")
