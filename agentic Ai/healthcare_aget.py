from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.websearch import WebSearchTools
from agno.tools.toolkit import ToolKit 

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,
        tools=[DuckDuckGoTools(), ToolKit()],
        description=(
            "You are a helpful assistant. "
            "For general queries, provide clear answers. "
            "For health queries, explain the condition, why it happens, "
            "how it can be treated, and what lifestyle changes help. "
            "Always remind the user to consult a doctor for medical advice."
        ),
        instructions=[
            "Use given tools whenever possible.",
            "For health queries: explain the problem, causes, and safe treatments.",
            "Mention common safe medicines only if widely accepted (like paracetamol for fever).",
            "Always remind the user to consult a qualified doctor for proper treatment.",
            "Format responses using markdown and use tables where possible."
        ],
        add_datetime_to_context=True
    )

open_agent = build_agent()
user_query = input("Enter your question: ")

try:
    open_agent.print_response(user_query, markdown=True)
except Exception as e:
    print("No results found, please try another query.")
