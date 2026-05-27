from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'answer the follwoing question {question} from ythe following text - {text}',
    input_variables = ['question', 'text']
)

chain = prompt | model | parser

result = chain.invoke({'question': 'whats the text about?', 'text': docs[0].page_content})

print(result)