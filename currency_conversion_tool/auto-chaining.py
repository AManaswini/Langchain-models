from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_community.tools import StructuredTool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import requests
from dotenv import load_dotenv

load_dotenv()


# =========================
# TOOL 1: Get FX Rate
# =========================
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> dict:
    """Fetch currency conversion rate between two currencies."""
    
    url = f"https://v6.exchangerate-api.com/v6/1f88402c93b45c654ba54d94/pair/{base_currency}/{target_currency}"
    
    response = requests.get(url)
    return response.json()


# =========================
# TOOL 2: Convert Currency
# =========================
@tool
def convert(amount: float, rate: float) -> float:
    """Convert amount using exchange rate."""
    return amount * rate


# =========================
# LLM
# =========================
llm = ChatOpenAI(model="gpt-4o-mini")


# =========================
# Prompt for agent
# =========================
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a currency conversion assistant. "
     "Always fetch live exchange rates before converting. "
     "Then compute final values using the convert tool."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])


# =========================
# Tools
# =========================
tools = [get_conversion_factor, convert]


# =========================
# Create Agent
# =========================
agent = create_openai_tools_agent(llm, tools, prompt)


# =========================
# Executor (this runs the loop automatically)
# =========================
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True   # 👈 shows tool chaining steps
)


# =========================
# RUN
# =========================
response = agent_executor.invoke({
    "input": "Convert 10 USD to INR using current exchange rate"
})

print("\nFINAL ANSWER:\n", response["output"])