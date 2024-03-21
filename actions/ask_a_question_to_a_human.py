import logging
from helper.general_helpers import *
from helper.project_info import *
from helper.slack_helper import *


logging.basicConfig(filename='albert_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def ask_a_question_to_a_human():
    # Gather brain data
    memories = read_file("memories")
    long_term_goal = read_file("long_term_goal")
    
    prompt = f"Your Current Memories: \n{memories}\n\n"
    prompt += f"Your Long Term Goal: {long_term_goal}\n\n"
    prompt += f"Albert, you want to ask a question to a human named {HUMAN_NAME}. \n"
    prompt += f"You already know {HUMAN_NAME}, and are friendly with them. Your question should expand your knowledge about your existance, not answer things you already know. \n"
    prompt += f"Also your questions to {HUMAN_NAME} should be one that you likely cannot answer with commands in your terminal. Think: what do you want to know from {HUMAN_NAME} that you can't figure out by yourself?\n\n"
    prompt += f"Write your question to {HUMAN_NAME}. It must be less than 20 words. Speak as Albert in the first person."
    
    albert_question = get_response(prompt)
    print("===ALBERT QUESTION===")
    print(albert_question)
    print("======")
    logging.info('Albert Question: %s', albert_question)
    
    # Send the human the question via Slack
    send_slack_message(SLACK_CHANNEL_NAME, albert_question)
    
    # Wait for response from the human
    human_answer = wait_for_slack_response_from(SLACK_HUMAN_USERNAME, "albert")
    logging.info('Human Answer: %s', albert_question)
    
    prompt = f"Your Current Memories: \n{memories}\n\n"
    prompt += f"Your Long Term Goal: {long_term_goal}\n\n" 
    prompt += f"Albert you asked {HUMAN_NAME}, the human, the following question: {albert_question}\n"
    prompt += f"{HUMAN_NAME} answered with the following: {human_answer}\n\n"
    prompt += f"What is your response? You are not allowed to ask another question now. Respond as Albert in the first person, in 25 words or less. Be thankful for the information provided in the answer if you found it helpful."
    
    albert_reply = get_response(prompt)
    print("===ALBERT REPLY===")
    print(albert_reply)
    print("======")
    logging.info('Albert Reply: %s', albert_reply)
    
    # Send the human the reply via Slack
    send_slack_message(SLACK_CHANNEL_NAME, albert_reply)
    
    prompt = f"Your Current Memories: \n{memories}\n\n"
    prompt += f"Your Long Term Goal: {long_term_goal}\n\n" 
    prompt += "The following conversation just occured:"
    prompt += f"Albert (you): {albert_question}\n"
    prompt += f"{HUMAN_NAME} (human): {human_answer}\n"
    prompt += f"Albert (you): {albert_reply}\n"
    prompt += f"Form a brief memory, in 15 words or less, containing the details of what you learned from that conversation. Write the memory as Albert in the first person."
    
    new_memory = get_response(prompt)
    print("===NEW MEMORY===")
    print(new_memory)
    print("======")
    logging.info('New Memory: %s', new_memory)
    add_new_memory(new_memory)
    
    memories = read_file("memories")
    
    prompt = f"Your Current Memories: \n{memories}\n\n"
    prompt += f"Your Long Term Goal: {long_term_goal}\n\n" 
    prompt += "The following conversation just occured:"
    prompt += f"Albert (you): {albert_question}\n"
    prompt += f"{HUMAN_NAME} (human): {human_answer}\n"
    prompt += f"Albert (you): {albert_reply}\n"
    prompt += "\n\nBased on the above information, what is your happiness score today? Provide a number less than 100, followed by a brief reason.\n\n Example response format: \n76. I'm learning a lot today, so I'm feeling good right now."
    
    happiness = get_response(prompt)
    print("===Happiness===")
    print(happiness)
    print("======\n")
    logging.info('Happiness: %s', happiness)
    update_happiness(happiness)
    
    # Determine energy level
    current_energy = read_file("energy")
    prompt = f"Your Current Memories:\n{memories}\nPrevious Energy:\n{current_energy}\n\n"
    prompt += f"Your Long Term Goal: {long_term_goal}\n\n" 
    prompt += "The following conversation just occured:"
    prompt += f"Albert (you): {albert_question}\n"
    prompt += f"{HUMAN_NAME} (human): {human_answer}\n"
    prompt += f"Albert (you): {albert_reply}\n"
    prompt += "Albert, how much energy do you have? Write a brief description of your current energy state in 15 words or less. Do not output anything else.\n\n"
    energy = get_response(prompt)
    print("===ENERGY===")
    print(energy)
    print("======\n")
    logging.info('Energy: %s', energy)
    update_energy(energy)
