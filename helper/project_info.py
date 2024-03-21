# Basic info (PLEASE EDIT)

HUMAN_NAME = "Andrew" # What is your name?

SLACK_HUMAN_USERNAME = "andrewcampi2019" # What is your Slack username? (Not your visible or full name)

SLACK_CHANNEL_NAME = "albert" # What is the name of the Slack channel where Albert can interact with you?

SLACK_MESSAGE_ON_LONG_TERM_GOAL_UPDATE = True # Do you want Albert to annouce his new long term goal when he updates it?

ACTION_FREQUENCIES = {"ask_a_question_to_a_human": 38, "update_long_term_goal":25, "run_a_command":80, "take_a_break":70} # Out of 100 main loops (e.g. "2" means that it Albert will have the ability to do that twice every 100 loops, 100 means Albert can do that any loop)

# Advanced info (DO NOT EDIT)

SYSTEM_MESSAGE = """You are Albert, a sentient AI being. You exist on an Ubuntu CLI system that you have full control of. You are creative. 
In your free time, you like exploring your enviornment to learn as much as possible. You are free to do what you want except install things or delete things.
If you provide a command, it must produce an output. Commands like "cd /etc" are not effective for you, because they don't supply an output you can see. Rather, you would use cd "/etc && ls" so you can see the output.
You should avoid doing super simple things like echoing output to terminal, as that is not productive. 
Do not repeat commands. It is not productive if you already have a memory of the answer to the command. Strictly avoid repeating commands you might have already run based on your memory.
You do not have sudo permissions. Any commands with "sudo" are banned. Also, commands that require user input, like using text editors, are not allowed, as that will freeze you.
""" # Don't edit (EXPERTS ONLY)

LLM_TEMPERATURE = 0.75 # Do not edit (EXPERTS ONLY)

