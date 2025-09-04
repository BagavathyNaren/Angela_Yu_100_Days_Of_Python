def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

import anthropic

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

def llm_model(prompt_txt, params=None):

    
    # Initialize Anthropic client with environment variable and custom HTTP client
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    )
    
    # Default parameters for Claude
    default_params = {
        "max_tokens": 256,
        "temperature": 0.5,
        "top_p": 0.2,
        "top_k": 1
    }
    
    if params:
        default_params.update(params)
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=default_params["max_tokens"],
            temperature=default_params["temperature"],
            top_p=default_params["top_p"],
            top_k=default_params["top_k"],
            messages=[
                {
                    "role": "user",
                    "content": prompt_txt
                }
            ]
        )
        
        # If response.content is a string, return it directly
        if isinstance(response.content, str):
            return response.content
        # If response.content is a list of blocks, join the 'text' from blocks that have it
        elif isinstance(response.content, list):
            return "".join(getattr(block, "text", "") for block in response.content if hasattr(block, "text"))
        else:
            return str(response.content)
        
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return None



params = {
"max_new_tokens": 512,
}
prompt = """How to deploy the crewai on crew ai enterprise website without any hassle?
Provide three independent explanations, then determine the most consistent result.
"""
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")