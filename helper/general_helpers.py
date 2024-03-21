import re
from helper.llm_endpoint import llm_endpoint_call
from helper.project_info import *


def format_input(prompt, system):
    if system == None:
        system_message = SYSTEM_MESSAGE
    else:
        system_message = system
    full_prompt = f"""<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant"""
    return full_prompt


def format_output(response):
    # Check for "assistant" or "user" at the start of a line in any capitalization and crop
    crop_pattern = re.compile(r'^\s*(assistant|user)', re.IGNORECASE | re.MULTILINE)
    crop_match = crop_pattern.search(response)
    if crop_match:
        response = response[:crop_match.start()]
    
    # Remove leading whitespaces and new lines
    formatted_response = re.sub(r'^\s+', '', response, flags=re.MULTILINE)

    # Remove trailing whitespaces and new lines
    formatted_response = re.sub(r'\s+$', '', formatted_response, flags=re.MULTILINE)
    
    # Remove leading ": " (if it exists)
    formatted_response = re.sub(r'^: ', '', formatted_response, flags=re.MULTILINE)

    return formatted_response


def get_response(prompt, system=None, max_tokens=None):
    prompt = format_input(prompt, system)
    
    if max_tokens == None:
        max_tokens = 8000

    response = llm_endpoint_call(prompt, max_tokens)

    # Check for a successful response
    if response.status_code == 200:
        response_data = response.json()
        return format_output(response_data['choices'][0]['text'])
    else:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")


def parse_response(response):
    # Initialize with default values for all expected sections
    parsed_data = {
        "happiness_score": "",
        "happiness_reason": "",
        "command": "",
        "reason_for_command": "",
        "current_memories": "",
        "long_term_goal":""
    }

    # Pattern to match sections more flexibly
    pattern = r"===(.+?)===\n(.*?)\n======"
    matches = re.findall(pattern, response, re.DOTALL)

    for header, content in matches:
        # Normalize the header to match keys in parsed_data
        normalized_header =  header.lower().replace(" ", "_")
        # Attempt to match normalized header with known keys, allowing for variations
        for key in parsed_data.keys():
            if normalized_header in key or key in normalized_header:
                parsed_data[key] = content.strip()
                break

    return parsed_data


def add_new_memory(memory):
    # Open the file in append mode
    with open('alberts_brain/memories.txt', 'a') as file:
        # Append the new memory followed by a newline character
        file.write(f"- {memory}\n")
        

def update_happiness(happiness):
    with open('alberts_brain/happiness.txt', "w") as file:
        file.write(happiness)


def update_energy(energy):
    with open('alberts_brain/energy.txt', "w") as file:
        file.write(energy)


def read_file(filename):
    path = f"alberts_brain/{filename}.txt"
    with open(path, "r") as f:
        contents = f.read()
    return contents
