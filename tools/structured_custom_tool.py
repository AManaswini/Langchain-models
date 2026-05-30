from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


# pydantic model enforcing datatype, isrequired and description
class MultiplyInput(BaseModel):
    a: int = Field(required = True, description = 'the first number to multiply')
    b: int = Field(required = True, description = 'the second number to multiply')


def multiply(a,b):
    return a*b

# define tool by using function, pydantic model to enforce args schema
multiply_tool = StructuredTool.from_function(
    func = multiply,
    name = 'multiply',
    description = 'multiply two numbers',
    args_schema = MultiplyInput
)

print(multiply_tool.invoke({'a':2,'b':3}))