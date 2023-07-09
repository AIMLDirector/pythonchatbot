#!/usr/bin/python3
import re
import random_responses
import json


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot_json")

def bot_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    for response in response_data:
        response_score = 0
        required_score = 0
        required_word = response["required_words"]

        if required_word:
            for word in split_message:
                if word in required_word:
                    required_score += 1

        if required_score == len(required_word):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1
        
        score_list.append(response_score)

        best_response = max(score_list)
        response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
            return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
            return response_data[response_index]["bot_response"]

    return random_responses.random_string()

while True:
    user_input = input("You:")
    print("Bot:", bot_response(user_input))


