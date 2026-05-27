from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Give a joke on the {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_generator = RunnableSequence(prompt1, model, parser)
prompt2 = PromptTemplate(
    template = 'Explain the following {joke}',
    input_variables = ['joke']
)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})



final_chain = RunnableSequence(joke_generator, parallel_chain)

print(final_chain.invoke({'topic': 'AI'}))