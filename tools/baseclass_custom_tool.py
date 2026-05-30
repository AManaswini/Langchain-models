from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


# pydantic model enforcing datatype, isrequired and description
class MultiplyInput(BaseModel):
    a: int = Field(required = True, description = 'the first number to multiply')
    b: int = Field(required = True, description = 'the second number to multiply')


class MultiplyTool(BaseTool):
    name: str = 'Multiply'
    description: str = 'Multiply two numbers'

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self,a,b):
        return a*b
    
multiply_tool = MultiplyTool().invoke({'a':3, 'b':2})
print(multiply_tool)
