from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from dotenv import load_dotenv
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

# tool and llm
search_tool = DuckDuckGoSearchRun()
llm = ChatOpenAI()
prompt = ChatPromptTemplate(
    ("system",
     "You are a helpful assistant. "
     "Always fetch current data and provide results."),
    ("human", "{input}")
)

agent = create_openai_tools_agent(
    model = llm,
    tools=[search_tool],
    system_prompt= prompt
)

agent_executor = AgentExecutor(agent=agent, tools = [search_tool], verbose = True)

results = agent_executor.invoke({'input': '3 ways to spend this weekend in milpitas'})

print(results)