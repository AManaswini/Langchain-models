from langchain_core.tools import tool

# # step 1 - create a function with docstring describing the function
# def multiply(a,b):
#     """ multiply two numbers"""
#     return a*b

# # step 2 - add type hints
# def multiply(a:int, b:int) -> int:
#     """multiply two numbers"""
#     return a*b

# step 3 - add tool decorator so that llm can use this

@tool
def multiply(a:int, b:int)-> int:
    """multiply two numbers"""
    return a*b

result = multiply.invoke({'a': 2, 'b': 3})

# print(result)

# print(multiply.name)
# print(multiply.args)
# print(multiply.description)

print(multiply.args_schema.model_json_schema())