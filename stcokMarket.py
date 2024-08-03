#this does not stop keep doing

# IMPORT REQUIRED LIBRARIES
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.tools import DuckDuckGoSearchRun

# SETUP SEARCH TOOL AND INITIALIZE MODEL
search_tool = DuckDuckGoSearchRun()

ollama_llm = Ollama(
    model="llama3",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

# DEFINE AGENTS WITH ROLES AND GOALS
researcher = Agent(
    role='Researcher',
    goal='Search the internet for the top 10 companies and their stock prices',
    backstory="""
    You are a financial researcher. Your goal is to find and report the top 10 companies by market capitalization along with their current stock prices.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

writer = Agent(
    role='Financial Content Writer',
    goal='Create an engaging article based on the research data provided',
    backstory="""You are a content writer specializing in financial topics. 
    You transform complex financial data into accessible and engaging narratives.""",
    verbose=True,
    allow_delegation=True,
    llm=ollama_llm
)

# CREATE TASKS FOR AGENTS
task1 = Task(
    description="""Find the top 10 companies by market capitalization and their current stock prices.
    Your final answer MUST be a list of companies with their stock prices""",
    expected_output="List of top 10 companies with their stock prices", 
    agent=researcher
)

task2 = Task(
    description="""Using the data provided by the researcher, write an engaging article about the top 10 companies and their stock performance.
    The article should explain why these companies are at the top and provide some insights into their stock performance.
    Make it informative and accessible to a general audience.""",
    expected_output="Full article of at least 4 paragraphs", 
    agent=writer
)

# INSTANTIATE CREW WITH A SEQUENTIAL PROCESS
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2, # You can set it to 1 or 2 for different logging levels
)

# GET YOUR CREW TO WORK
result = crew.kickoff()

print("###########")
print(result)
