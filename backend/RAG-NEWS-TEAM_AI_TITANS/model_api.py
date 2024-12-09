import os
import replicate
import config


class ModelAPI:
    """
    Scalable API for accessing models hosted on Replicate AI.
    """
    def __init__(self, model_name, api_token=config.REPLICATE_API_KEY):
        os.environ['REPLICATE_API_TOKEN'] = api_token
        self.model_name = model_name
        self.params = {
            "top_p": 0.95,
            "prompt": "",
            "max_new_tokens": 3,
            "temperature": 0.2,
            "frequency_penalty": 1,
            "template": '''
            <s>[INST] {prompt}
            
ANSWER STRICTLY IN ONE WORD.  
            \nWhich category does the statement belong to: 
            1. Technology\n 2. Sports\n 3. Science\n 4. Health\n
            [/INST] 
            '''
        }

    def execute(self, input_prompt) -> list:
        self.params['prompt'] = input_prompt
        result = replicate.run(self.model_name, self.params)
        return result


if __name__ == '__main__':
    api = ModelAPI(model_name='mistralai/mixtral-8x7b-instruct-v0.1')
    output = api.execute("NASA Rocket Launch")
    print(output)