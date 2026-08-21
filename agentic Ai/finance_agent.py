from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,
        tools=[YFinanceTools(), DuckDuckGoTools()],
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=[
            "Use given tools whenever possible. Format your response using markdown and use tables to display data where possible."
        ],
        add_datetime_to_context=True
    )

if __name__ == "__main__":
    open_agent = build_agent()
    
    while True:
        user_query = input("Enter your question (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("Exiting agent...")
            break
        open_agent.print_response(user_query, markdown=True)
