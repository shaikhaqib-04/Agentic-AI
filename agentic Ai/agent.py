from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools
from agno.tools.websearch import WebSearchTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,
        tools=[DuckDuckGoTools(), WebSearchTools()], 
        instructions="You are a helpful assistant that provides information and answers questions based on the provided context.",
        add_datetime_to_context=True
    )

open_agent = build_agent()
user_query = input("Enter your question: ")

try:
    open_agent.print_response(user_query)
except Exception as e:
    print("No results found, please try another query.")
