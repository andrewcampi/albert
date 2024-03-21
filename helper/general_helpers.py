import re
from helper.llm_endpoint import llm_endpoint_call
from helper.project_info import *


def get_response(prompt, max_tokens=None):
    
    if max_tokens == None:
        max_tokens = 8000

    response = llm_endpoint_call(prompt, max_tokens)

    return response


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
    
    # Process the "memories" file to return only the last 25 lines
    if filename == "memories":
        lines = contents.splitlines()  # Split the contents into a list of lines
        if len(lines) > 25:
            lines = lines[-25:]  # Keep only the last 25 lines if there are more than 25
        contents = "\n".join(lines)  # Join the lines back into a string
    
    return contents
