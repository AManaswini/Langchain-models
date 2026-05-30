# Tool for fetching conversion factor

# Multiplication tool


# tool create

from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
import requests
from dotenv import load_dotenv
from langchain_core.tools import InjectedToolArg
from typing import Annotated

load_dotenv()

# create tools
@tool
def get_conversion_factor(base_currency: str, target_currency:str)-> float:
    """this function fetches the currency conversion factor between base and target currencies"""
    url = f'https://v6.exchangerate-api.com/v6/1f88402c93b45c654ba54d94/pair/{base_currency}/{target_currency}'
    response = requests.get(url=url)
    return response.json()

result = get_conversion_factor.invoke({'base_currency': 'USD', 'target_currency': 'INR'})

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg])-> float:
    """given a conversion rate, this function calculates atrget currency value from base value"""
    return base_currency_value * conversion_rate


# TOOL BINDING

llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])


messages = [HumanMessage('can you tell mw whats the current conversion rate between USD and INR, can you convert 10 INR to USD based on that?')]


# TOOL CALLING for suggestion
ai_message = llm_with_tools.invoke(messages)
print(ai_message.tool_calls)
messages.append(ai_message)

# TOOL EXECUTION
tool_call = ai_message.tool_calls[0]

result = get_conversion_factor.invoke(tool_call['args'])

conversion_rate = result['conversion_rate']

tool_message = ToolMessage(
    content=str(result),
    tool_call_id = tool_call['id']
)
messages.append(tool_message)

# invoke convert with the conversion rate from above
resultf = convert.invoke({
    "base_currency_value": 10,
    "conversion_rate": conversion_rate
})

print(resultf)


messages.append(HumanMessage(content =f'final converted value is {resultf} USD'))
final_response = llm_with_tools.invoke(messages)
print(final_response.content)