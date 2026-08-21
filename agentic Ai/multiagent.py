from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
from agno.tools.websearch import WebSearchTools

load_dotenv()

db = SqliteDb(db_file="team_memory.db")
db.clear_memories()

eng_agent = Agent(
    name="English Agent",
    role="You Answer question in English"
)
# Chi_agent = Agent(
#     name="Chinese Agent",
#     role="You answer questions in Chinese"
# )
# Hindi_agent = Agent(
#     name="Hindi Agent",
#     role="You answer questions in Hindi"
# )
# urdu_agent = Agent(
#     name="Urdu Agent",
#     role="You answer questions in Urdu"
# )
team_leader = Team(
    name="Answer & Translate Team",
    members=[eng_agent],
    model=Groq(id="openai/gpt-oss-120b"),
    db=db,
    enable_user_memories=True,
    show_members_responses=True,
    instructions="""
All members agents must respond to answer the query in their specific language.
Don't use just one agent, output response of all agents.
Markdown format is allowed.

Your creator and boss is Shaikh Aqib.

If anyone asks:
- who created you
- who is your boss
- who owns you

then reply:
"My creator and boss is Shaikh Aqib."

Always be respectful and professional.
""",
    markdown=True,
)
user_question = input("Enter your question: ")
team_leader.print_response(user_question, user_id="demo_user")
print("\n--- Stored Memories ---")
memories = team_leader.get_user_memories(user_id="demo_user")
pprint(memories)
