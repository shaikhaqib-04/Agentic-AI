from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
# from agno.tools import 

load_dotenv()

db = SqliteDb(db_file="memory.db")  
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        enable_user_memories=True,  # to enable memory functionality
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,  # formatted markdown responses
        add_history_to_context=True,  # add conversation history in the context
        # instructions="""
        # YOU ARE A HELPFUL AND EXPERT TRAVEL AGENT.
        # YOU PROVIDE INFORMATION ABOUT TRAVEL DESTINATIONS,
        # FLIGHTS, HOTELS, AND ACTIVITIES.
        # ANSWER QUESTIONS ...
        # """
    )

user_id = "shaikhaqib"
Open_agent = build_agent()  
Open_agent.print_response("I am a intern",user_id=user_id,)
Open_agent.print_response("Who am I ?",user_id=user_id,)
memories = Open_agent.get_user_memories(user_id=user_id) 

print("memories:")
pprint(memories)