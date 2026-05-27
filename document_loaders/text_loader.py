from langchain_community.document_loaders import TextLoader
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, "cricket.txt")

loader = TextLoader(file_path, encoding='utf-8')

docs = loader.load()

content = docs[0].page_content

prompt = PromptTemplate(
    template ='generate a summary on {text}',
    input_variables =['text']
)

chain = prompt | model | parser

print(chain.invoke({'text': content}))