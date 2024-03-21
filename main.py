# General imports
import logging
# Helper imports
from helper.general_helpers import *
from helper.llm_endpoint import *
from helper.project_info import *
from helper.project_secrets import *
from helper.slack_helper import *
# Action imports
from actions.ask_a_question_to_a_human import ask_a_question_to_a_human
from actions.update_long_term_goal import update_long_term_goal
from actions.run_a_command import run_a_command
from actions.take_a_break import take_a_break


logging.basicConfig(filename='albert_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Calculate intervals for each action based on its frequency
action_intervals = {action: max(1, round(100 / frequency)) for action, frequency in ACTION_FREQUENCIES.items()}

# Initialize a counter for loop iterations
loop_iteration = 1

# Main Loop
while True:
    # Read memories
    memories = read_file("memories")
    prompt = f"Your Current Memories:\n{memories}\n"
    current_energy = read_file("energy")
    prompt += f"Your Current Energy:\n{current_energy}\n"
    prompt += "\nAlbert, you now get to select which action to take. You are free to choose whichever one you want from the below list:\n"

    # Initialize a list to keep track of available actions
    available_actions = []

    # Check each action for availability based on the current loop iteration
    for action, interval in action_intervals.items():
        if loop_iteration % interval == 0:
            available_actions.append(action)

    # Ensure at least one action is always available
    if not available_actions:
        available_actions.append("run_a_command")  # Default action if none are available based on frequency

    # Build the prompt with available actions
    for idx, action in enumerate(available_actions, start=1):
        if action == "ask_a_question_to_a_human":
            prompt += "1. ask_a_question_to_a_human : Use this option if you have a question you would like to ask a human.\n"
        elif action == "update_long_term_goal":
            prompt += "2. update_long_term_goal: Use this option if you want to change your long term goal.\n"
        elif action == "run_a_command":
            prompt += "3. run_a_command: Use this option to run a command in the terminal.\n"
        elif action == "take_a_break":
            prompt += "4. tak_a_break: Are you tired? Need a break? Use this option.\n"
    
    prompt += "\n\nWhat would you like to do? State the option number, followed by the option name. You can only choose one. Do not output anything else.\n\n"
    prompt += "Example Response #1:\n 3. run_a_command\n"
    prompt += "Example Response #2:\n 4. take_a_break\n"
    
    albert_action_choice = get_response(prompt)
    print("===ACTION===")
    print(albert_action_choice)
    print("======")

    # Increment the loop iteration
    loop_iteration += 1
    
    # Run the action
    if "1." in albert_action_choice and "ask_a_question_to_a_human" in albert_action_choice:
        logging.info('Action: %s', "Albert wants to ask a question to a human.")
        ask_a_question_to_a_human()
    
    elif "2." in albert_action_choice and "update_long_term_goal" in albert_action_choice:
        logging.info('Action: %s', "Albert wants to update the long term goal.")
        update_long_term_goal()
    
    elif "3." in albert_action_choice and "run_a_command" in albert_action_choice:
        logging.info('Action: %s', "Albert wants to run a command.")
        run_a_command()
    
    elif "4." in albert_action_choice and "take_a_break" in albert_action_choice:
        logging.info('Action: %s', "Albert wants to take a break.")
        take_a_break()

    
