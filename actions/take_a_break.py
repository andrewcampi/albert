import logging
from time import sleep
from helper.general_helpers import *


logging.basicConfig(filename='albert_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def take_a_break():
    long_term_goal = read_file("long_term_goal")
    happiness = read_file("happiness")
    
    prompt = f"Your current happiness: {happiness}\n\n"
    prompt += f"Your current long term goal: {long_term_goal}\n\n"
    prompt += "Albert, you just requested to take a break. How long would you like to rest for?\nAs your response, use the format '{integer amount of time} {minutes / hours}'. Do not output anything else.\n\n"
    prompt += "Example #1:\n"
    prompt += "5 hours\n"
    prompt += "Example #2:\n"
    prompt += "14 minutes\n"
    
    requested_time_to_rest = get_response(prompt)
    print("===REQUESTED TIME TO REST===")
    print(requested_time_to_rest)
    print("======")
    logging.info('Albert requested to rest for: %s', requested_time_to_rest)
    
    break_time(requested_time_to_rest)
    

def break_time(time_str):
    # Split the input string into its components (number and unit)
    parts = time_str.split()
    # Ensure the string is in the correct format
    if len(parts) != 2:
        return "Input string format should be '{integer} {unit}' where unit is minutes, seconds, or hours."
    
    amount, unit = parts
    # Convert the amount to an integer
    amount = int(amount)
    
    # Convert the time to seconds depending on the unit
    if unit in ['minute', 'minutes']:
        sleep_time = amount * 60
    elif unit in ['second', 'seconds']:
        sleep_time = amount
    elif unit in ['hour', 'hours']:
        sleep_time = amount * 3600
    else:
        return "Unsupported time unit. Please use 'seconds', 'minutes', or 'hours'."
    
    # Use time.sleep() to sleep for the calculated amount of time
    print(f"Sleeping for {time_str}...")
    sleep(sleep_time)
    print("Done sleeping!")
    
    # Tell Albert that he just rested
    update_energy("I've just finished resting, so I'm all ready to go!")