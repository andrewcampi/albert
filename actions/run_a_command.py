import logging
from subprocess import Popen, PIPE
from helper.general_helpers import *


logging.basicConfig(filename='albert_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def safe_subprocess_run(cmd, byte_limit=10000):
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, text=True)
    stdout, stderr = process.communicate()
    truncated_stdout = (stdout[:byte_limit] + '...') if len(stdout) > byte_limit else stdout
    return truncated_stdout, stderr, process.returncode


def run_a_command():
    memories = read_file("memories")
    
    prompt = f"Your Current Memories: \n{memories}"
    prompt += "\n\nAlbert, what command would you like to execute? Remember, your command should expand your knowledge, not repeat things you already know. Simply state the command. Do not output anything else. I should be able to copy and paste your output directly as a working command."
    prompt += "\n\nExample response:\npwd # Outputs the content of the CWD."
        
    command = get_response(prompt)
    print("===COMMAND===")
    print(command)
    print("======")
    logging.info('Command: %s', command)
    
    prompt = f"Your Current Memories: \n{memories}\nCommand to execute:{command}"
    prompt += f"You, Albert, told me to execute the above command. Can you explain why (in one sentence) you want to execute that command specifically? Speak in the first person as Albert."
    cmd_reason = get_response(prompt)
    print("===CMD REASON===")
    print(cmd_reason)
    print("======")
    logging.info('CMD Reason: %s', cmd_reason)
    
    output, stderr, returncode = safe_subprocess_run(command)
    if len(output) <= 3:
        output = str(stderr)
        if len(output) <= 3:
            output = "[The commnad provided no visible output, but no error either]"
    print("===OUTPUT===")
    print(output)
    print("======")
    logging.info('Output: %s', output)
    
    prompt = f"Your Current Memories: \n{memories}\nExecuted command:{command}\nOutput:{output}"
    prompt += "\n\nWhat did you, Albert, learn from the above command output? Write one very specific note in 15 words or less, containing the details from the command's output. Write in the first person as Albert."
    new_memory = get_response(prompt)
    print("===New Memory===")
    print(new_memory)
    print("======")
    add_new_memory(new_memory)
    logging.info('New Memory: %s', new_memory)
    
    # Read memories
    memories = read_file("memories")
    
    # Determine happiness level
    prompt = f"Your Current Memories: \n{memories}\nExecuted command:{command}\nOutput:{output}\n\n"
    prompt += "\n\nBased on the above information, what is your happiness score today? Provide a number less than 100, followed by a brief reason.\n\n Example response format: \n45. My commands are not working lately, so I'm upset."
    happiness = get_response(prompt)
    print("===HAPPINESS===")
    print(happiness)
    print("======\n")
    logging.info('Happiness: %s', happiness)
    update_happiness(happiness)
    
    current_energy = read_file("energy")
    
    # Determine energy level
    prompt = f"Your Current Memories:\n{memories}\nPrevious Energy:\n{current_energy}\n\nExecuted command:{command}\nOutput:{output}\n\n"
    prompt += "Albert, how much energy do you have? Write a brief description of your current energy state in 15 words or less. Do not output anything else.\n\n"
    energy = get_response(prompt)
    print("===ENERGY===")
    print(energy)
    print("======\n")
    logging.info('Energy: %s', energy)
    update_energy(energy)
    