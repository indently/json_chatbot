import json
import re


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        # Check if there are any required words
        if response["required_words"]:
            for word in split_message:
                if word not in response["required_words"]:
                    break  # If not, exit response.

        # Check each word the user has typed
        for word in split_message:
            # If the word is in the response, add to the score
            if word in response["user_input"]:
                response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        print(response_score, response["user_input"])

    best_response = max(score_list)
    response_index = score_list.index(best_response)
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return "I didn't understand what you wrote!"


while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))
