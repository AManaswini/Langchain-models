class NakliLLM:
    def __init(self):
        print('LLM created successfully')

    def predict(self, prompt):
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        return {'response': random.choice(response_list)}
    
llm = NakliLLM()

llm.predict('any random question')

class NakliPromptTemplate:
    def __int__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
template = NakliPromptTemplate(
    template = 'Write. a poem about {topic}',
    input_variables = ['topic']
)

template.format({'topic':'India'})