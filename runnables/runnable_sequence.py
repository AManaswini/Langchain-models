from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()


# RUNNABLES

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'explain the following joke = {text}',
    input_varibales = ['joke']
)

parser = StrOutputParser()

model = ChatOpenAI()

#RUNNABLE SEQUENCE
chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

print(chain.invoke({'topic': 'AI'}))