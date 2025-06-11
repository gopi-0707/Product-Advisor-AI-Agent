import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import initialize_agent, Tool
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from database import search_products

@tool
def product_tool(query: str) -> str:
    """Searches mock product database based on user query."""
    return search_products(query)

def create_agent():

    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
    )
    
    tools = [
        Tool.from_function(
            func=product_tool,
            name="ProductSearch",
            description="Searches the product database for items matching user query"
        )
    ]
    agent = initialize_agent(tools, llm, agent_type="chat-zero-shot-react-description", verbose=True)
    return agent
