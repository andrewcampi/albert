from time import sleep
import requests # In this OpenAI example, we are not using this import
from helper.project_info import *
from helper.project_secrets import *

from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def llm_endpoint_call(prompt, max_tokens): # In this OpenAI example, we are not using max_tokens
    # Send the request to the API
    sleep(3.273484748383) # Sleep time that appears to be random/natural
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=LLM_TEMPERATURE,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content