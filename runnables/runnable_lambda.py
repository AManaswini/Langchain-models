from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_count)

# RUNNABLES

prompt1 = PromptTemplate(
    template = 'Generate a joke about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a linkedin post about {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_generator = RunnableSequence(prompt1, model , parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'wordcount': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_generator, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})

print(result)