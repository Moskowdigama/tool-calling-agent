"""
Multi-Agent Research System - Streamlit UI

Pipeline: Searcher → Reader → Writer → Critic
"""

import os
import streamlit as st
from core.orchestrator import run_multi_agent_pipeline


# Page config
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Multi-Agent Research System")
st.caption("Searcher → Reader → Writer → Critic")

# Sidebar for API keys
with st.sidebar:
    st.header("🔑 API Keys")
    
    mistral_key = st.text_input(
        "Mistral AI API Key",
        type="password",
        help="Get your API key from https://console.mistral.ai/"
    )
    
    tavily_key = st.text_input(
        "Tavily API Key",
        type="password",
        help="Get your API key from https://tavily.com/"
    )
    
    if mistral_key:
        os.environ["MISTRAL_API_KEY"] = mistral_key
    if tavily_key:
        os.environ["TAVILY_API_KEY"] = tavily_key
    
    st.divider()
    st.markdown("### 🚀 About")
    st.markdown("""
    This system uses **4 specialized agents**:
    1. 🔍 **Searcher** - Finds relevant sources
    2. 📖 **Reader** - Extracts content from URLs  
    3. ✍️ **Writer** - Synthesizes research into a report
    4. 🎯 **Critic** - Reviews and improves the report
    """)

# Main interface
query = st.text_area(
    "🔍 What do you want to research?",
    placeholder="e.g., What are the latest advancements in AI-powered robotics?",
    height=100
)

col1, col2 = st.columns([1, 5])
with col1:
    run_button = st.button("🚀 Run Pipeline", type="primary", use_container_width=True)

# Process the query
if run_button:
    if not mistral_key:
        st.error("❌ Please enter your Mistral AI API key in the sidebar")
        st.stop()
    if not tavily_key:
        st.error("❌ Please enter your Tavily API key in the sidebar")
        st.stop()
    if not query:
        st.error("❌ Please enter a research query")
        st.stop()
    
    # Run the pipeline
    with st.spinner("🧠 Running multi-agent pipeline..."):
        try:
            result = run_multi_agent_pipeline(query, mistral_key)
            
            # Display results
            st.success("✅ Pipeline complete!")
            
            # Create tabs for different views
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📄 Final Report",
                "🔍 Search Results",
                "📖 Raw Content",
                "✍️ Draft Report",
                "🎯 Critic Review"
            ])
            
            with tab1:
                st.markdown("### 📄 Final Report (Critic-Reviewed)")
                final = result.get("final_output", "No final output")
                st.markdown(final)
            
            with tab2:
                st.markdown("### 🔍 Search Results")
                search_results = result.get("search_results", [])
                if search_results:
                    for i, item in enumerate(search_results, 1):
                        with st.expander(f"{i}. {item.get('title', 'Untitled')}"):
                            st.markdown(f"**URL:** {item.get('url', 'N/A')}")
                            st.markdown(f"**Relevance Score:** {item.get('score', 0):.2f}")
                            st.markdown("**Content:**")
                            st.markdown(item.get('content', 'No content')[:500] + "...")
                else:
                    st.info("No search results found")
            
            with tab3:
                st.markdown("### 📖 Raw Content Extracted")
                raw_content = result.get("raw_content", [])
                if raw_content:
                    for item in raw_content:
                        with st.expander(f"{item.get('title', 'Untitled')}"):
                            st.markdown(f"**URL:** {item.get('url', 'N/A')}")
                            st.markdown("**Content:**")
                            st.markdown(item.get('content', 'No content')[:1000] + "...")
                else:
                    st.info("No content extracted")
            
            with tab4:
                st.markdown("### ✍️ Draft Report (Before Critic)")
                draft = result.get("draft_report", "No draft")
                st.markdown(draft)
            
            with tab5:
                st.markdown("### 🎯 Critic Review")
                score = result.get("critic_score", "N/A")
                feedback = result.get("critic_feedback", "No feedback")
                
                col1, col2, col3 = st.columns([1, 2, 3])
                with col1:
                    if isinstance(score, int):
                        if score >= 8:
                            st.success(f"Score: {score}/10 ⭐")
                        elif score >= 5:
                            st.warning(f"Score: {score}/10")
                        else:
                            st.error(f"Score: {score}/10")
                    else:
                        st.info(f"Score: {score}")
                
                st.markdown("**Feedback:**")
                st.markdown(feedback)
                
                st.markdown("**Revised Report:**")
                revised = result.get("revised_report", "No revised report")
                st.markdown(revised)
            
            # Show agent logs
            with st.expander("📊 Agent Execution Logs"):
                logs = result.get("agent_logs", [])
                for log in logs:
                    st.json(log)
                    
        except Exception as e:
            st.error(f"❌ Error running pipeline: {str(e)}")
            st.exception(e)

# Footer
st.divider()
st.caption("Built with Streamlit · LangChain · Mistral AI · Tavily")
