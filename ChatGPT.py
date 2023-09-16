import openai
import json
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

API_KEY = "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"
messages = [
    {
        "role": "system",
        "content": "You are a diversity and inclusion consultant."
    },
    {
        "role": "user",
        "content": "Please evaluate our job listing for the given job position and provide feedback on how to make it more diverse and inclusive."
    },
    {
        "role": "assistant",
        "content": "Sure, please paste the job listing text here for evaluation."
    }
]
model = "gpt-3.5-turbo"

"""
try:
    with open('config.json', 'r') as config_json:
        config = json.load(config_json)
        if 'openAI API Key' in config:
            API_KEY = config['openAI API Key']
            has_access_token = True
        if 'messages' in config:
            messages = config['messages']
        if 'model' in config:
            model = config['model']
except FileNotFoundError:
    pass
except json.decoder.JSONDecodeError:
    pass
"""

openai.api_key = API_KEY

print(API_KEY)
print(messages)

my_message = input("Enter your job listing : ")


def new_message():
    messages.append(
        {"role": "user", "content": my_message},
    )

    # This will display while the API is processing
    print("Processing your request...")

    chat = openai.ChatCompletion.create(
        model=model, messages=messages
    )

    print("Response received!")  # This will display once the API responds

    reply = chat.choices[0].message.content

    print(f"ChatGPT: {reply}")


new_message()