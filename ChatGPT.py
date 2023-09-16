import openai
import json
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

API_KEY = ""
messages = []
model = ""

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
