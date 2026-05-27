from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'write a summary on {topic}',
    input_variables = ['topic']
)

report = RunnableSequence(prompt1, model, parser)

branch = RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(prompt2, model , parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report, branch)

print(final_chain.invoke({'topic':'AI'}))