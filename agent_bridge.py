import httpx
import json
import os

class AgentBridge:
    """
    Bridge class to handle communication between the Streamlit UI and 
    the Antigravity agent workflows.
    """
    
    def __init__(self, api_base_url=None, api_key=None):
        self.api_base_url = api_base_url or os.getenv("ANTIGRAVITY_API_URL")
        self.api_key = api_key or os.getenv("ANTIGRAVITY_API_KEY")

    async def invoke_agent(self, agent_id, prompt, context=None):
        """
        Invoke a specific agent with the given prompt.
        """
        # Placeholder for local simulation if no remote URL is provided
        if not self.api_base_url:
            return f"Simulation: {agent_id} processed '{prompt[:30]}...' in offline mode."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "agent_id": agent_id,
            "prompt": prompt,
            "context": context or {}
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_base_url}/invoke",
                    json=payload,
                    headers=headers,
                    timeout=30.0
                )
                response.raise_for_status()
                return response.json().get("output", "No response from agent.")
        except Exception as e:
            return f"Error connecting to Antigravity Cloud: {str(e)}"

# Example Usage:
# bridge = AgentBridge()
# result = await bridge.invoke_agent("/orchestrator_agent", "Plan my day")
