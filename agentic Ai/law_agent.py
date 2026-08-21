from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv


load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,
        tools=[DuckDuckGoTools()],
        description="You are a legal research assistant that generates structured law reports. You provide case summaries, statutes, precedents, arguments, and practical implications.",
        instructions=[
            "Always structure responses like a legal report.",
            "Use markdown tables for statutes and precedents.",
            "Provide clear, actionable insights in bullet points."
        ],
        add_datetime_to_context=True
    )

ai = build_agent()
user_query = input("Enter your question:")
ai.print_response(user_query)