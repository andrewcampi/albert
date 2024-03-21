import logging
from helper.project_info import *
from helper.general_helpers import *
from helper.slack_helper import *


logging.basicConfig(filename='albert_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def update_long_term_goal():
    memories = read_file("memories")
    long_term_goal = read_file("long_term_goal")
    happiness = read_file("happiness")
    
    prompt = f"Your Current Memories: \n{memories}\n\n"
    prompt += f"Your current happiness: {happiness}\n\n"
    prompt += f"Your current long term goal: {long_term_goal}\n\n"
    prompt += "Albert, you are free to update your long term goal to whatever you would like.\nAs your response, rewrite your long term goal. It should be concise. Only output one long term goal in less than 15 words. Do not output anything else."
    
    new_long_term_goal = get_response(prompt)
    print("===NEW LONG TERM GOAL===")
    print(new_long_term_goal)
    print("======")
    logging.info('New Long Term Goal: %s', new_long_term_goal)
    
    with open("alberts_brain/long_term_goal.txt", "w") as f:
        f.write(new_long_term_goal)
    
    if SLACK_MESSAGE_ON_LONG_TERM_GOAL_UPDATE:
        message = f'Hey {HUMAN_NAME}, I just wanted to let you know that I updated my long term goal to be the following: "{new_long_term_goal}"'
        send_slack_message(SLACK_CHANNEL_NAME, message)
    
    