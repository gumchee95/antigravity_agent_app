import streamlit as st
import time
import random

# Page Config
st.set_page_config(
    page_title="Antigravity Agent OS",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Custom CSS (Glassmorphism & Dark Mode)
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: radial-gradient(circle at top right, #1a1a2e, #162447, #1b1b2f);
        color: #e0e0e0;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Chat Message Container */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(5px);
        transition: transform 0.2s ease;
    }
    
    .stChatMessage:hover {
        transform: translateY(-2px);
        border-color: rgba(0, 150, 255, 0.5);
    }
    
    /* Header styling */
    h1 {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    /* Input field */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        color: white !important;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Application Logic
def main():
    st.title("🌌 Antigravity Agent OS")
    st.caption("Personalized Cloud Interface for Advanced Multi-Agent Collaboration")

    # Sidebar: Agent Catalog
    with st.sidebar:
        st.header("Available Agents")
        agent_type = st.selectbox(
            "Select Lead Agent:",
            ["/orchestrator_agent", "/finance_agent", "/ops_agent", "/tech_lead_agent", "/design_agent"]
        )
        st.divider()
        st.info("💡 Tip: Use `/orchestrator_agent` to coordinate multiple specialists for complex tasks.")
        
        if st.button("Reset Session"):
            st.session_state.messages = []
            st.rerun()

    # Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("How can I help you today?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Agent Execution Simulation
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Logic bridge placeholder
            prefix = f"[{agent_type}] Processing request..."
            message_placeholder.markdown(prefix + " ▌")
            
            time.sleep(1) # Simulate thinking
            
            # This is where the real Antigravity bridge would go
            responses = [
                f"I've analyzed your request using the {agent_type} module. Initial findings suggest a multi-layered approach.",
                "Based on the logic-driven framework, here are the atomic actions required...",
                "The system is currently scanning the context for relevant variables."
            ]
            assistant_response = random.choice(responses)
            
            # Typing animation
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
