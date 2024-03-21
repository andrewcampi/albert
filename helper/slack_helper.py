from time import sleep
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from helper.project_secrets import *


# Initialize with your bot token
client = WebClient(token=SLACK_TOKEN)


def get_latest_slack_message(channel_name):
    try:
        # Retrieve the ID of the channel by its name
        response = client.conversations_list()
        channel_id = next((item["id"] for item in response["channels"] if item["name"] == channel_name), None)
        if channel_id is None:
            return {"error": "Channel not found"}
        
        # Fetch the latest message from the channel
        result = client.conversations_history(channel=channel_id, limit=1)
        messages = result['messages']
        if not messages:
            return {"username": "No messages", "message": "No messages"}

        # Get user info to find username
        user_id = messages[0]['user']
        user_info = client.users_info(user=user_id)
        username = user_info['user']['name']

        return {"username": username, "message": messages[0]['text']}
    except SlackApiError as e:
        return {"error": f"Slack API Error: {e.response['error']}"}


def send_slack_message(channel_name, message):
    try:
        # Retrieve the ID of the channel by its name
        response = client.conversations_list()
        channel_id = next((item["id"] for item in response["channels"] if item["name"] == channel_name), None)
        if channel_id is None:
            return {"error": "Channel not found"}
        
        # Send message to the specified channel
        client.chat_postMessage(channel=channel_id, text=message)
        return {"success": True}
    except SlackApiError as e:
        return {"error": f"Slack API Error: {e.response['error']}"}


def wait_for_slack_response_from(username, channel_name):
    still_waiting = True
    while still_waiting:
        latest_slack_message = get_latest_slack_message(channel_name)
        if latest_slack_message["username"] == username:
            still_waiting = False
            return latest_slack_message["message"]
        else:
            sleep(7)