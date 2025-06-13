# This module defines the AI agent using LangChain and Google Gemini LLM.
import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import initialize_agent, Tool
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from database import search_products

# Define the product search tool for the agent
@tool
def product_tool(query: str) -> str:
    """Searches mock product database based on user query."""
    return search_products(query)

# Function to create and initialize the LangChain agent with the Gemini LLM
def create_agent():
    # Configure the Gemini model
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
    )

    # Define product_tool
    tools = [
        Tool.from_function(
            func=product_tool,
            name="ProductSearch",
            description="Searches the product database for items matching user query"
        )
    ]

    # Initialize a zero-shot reasoning agent with tool access
    agent = initialize_agent(tools, llm, agent_type="chat-zero-shot-react-description", verbose=True)
    return agent
