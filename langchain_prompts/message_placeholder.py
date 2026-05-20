from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


chat_template = ChatPromptTemplate(
    [
        ('system', 'Youre a helpful customer support agent'),
        MessagesPlaceholder(variable_name = 'chat_history')
        ('human', '{query}')
    ]
)

chat_history = []

# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

prompt = chat_template.invoke({
    'chat_history': chat_template, 
    'query': HumanMessage('where is my refund?')
    })

print(prompt)