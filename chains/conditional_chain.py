from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda

load_dotenv()

model = ChatOpenAI()

# analyse the feedback

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description='Give sentiment of the feedback')

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following review into positive or negative {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction': parser2.get_format_instructions()}
)
classifier_chain = prompt1 | model | parser2


prompt2 = PromptTemplate(
    template = 'Write an appropriate response to this positive feedback {feedback} ',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to this negative feedback {feedback} ',
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x:'couldnot find sentiment')
)

final_chain = classifier_chain | branch_chain 

result = final_chain.invoke({'feedback': 'this is a average example'})

print(result)

print(final_chain.get_graph().print_ascii())