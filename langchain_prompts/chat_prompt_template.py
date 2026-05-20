from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', 'Youre a helpful {domain} expert'),
    ('human', 'EXplain about {topic} in simple terms ')
])

prompt = chat_template.invoke({"domain": 'cricket', "topic":'IPL'})

print(prompt)