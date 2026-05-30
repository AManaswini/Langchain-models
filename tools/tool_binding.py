from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()


# tool is built
@tool
def multiply(a: int, b: int) -> int:
    """multiply two numbers"""
    return a * b


llm = ChatOpenAI()

# Bind tool with llm
llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage(content='multiply 2 with 3')

messages = [query]

# STEP 1: LLM decides tool call when invoked directly, it suggests which tool to use
result = llm_with_tools.invoke(messages)

messages.append(result)

# STEP 2: Execute tool based on suggestion from previous message
tool_call = result.tool_calls[0]

tool_result = multiply.invoke(tool_call['args'])

# STEP 3: Send tool result back to LLM to get human readable response
tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call['id']
)

# print(tool_message)
messages.append(tool_message)

# STEP 4: Final response from LLM in human readable form
final_result = llm_with_tools.invoke(messages)

print(final_result.content)