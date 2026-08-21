import streamlit as st
import requests
import os
import multiagent
from dotenv import load_dotenv

st.title("Agentic AI")

st.chat_input("Enter your query")