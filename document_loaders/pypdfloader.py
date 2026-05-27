from langchain_community.document_loaders import TextLoader, PyPDFLoader
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, "dl-curriculum.pdf")

loader = PyPDFLoader(file_path)

docs = loader.load()

print(docs[0])
