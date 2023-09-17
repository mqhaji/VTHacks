from flask import Flask, request, jsonify, render_template
import openai
import sys  # for command line arguments

app = Flask(__name__)

# openai api key
# openai.api_key = str(sys.argv[1])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python', methods=['POST'])
def run_python():
    api_key = request.form.get('api_key')  # Get the API key from the form
    user_input = "You are a diversity and inclusion consultant.\n"
    user_input += "Please evaluate our job listing for the given job position and provide feedback on how to make it more inclusive.\n"
    user_input += request.form.get('user_input')
    print(user_input)

    # Set the API key for OpenAI
    openai.api_key = api_key

    # Create a conversation with user input
    messages = [{"role": "system", "content": "You are an intelligent assistant."}]
    messages.append({"role": "user", "content": user_input})

    chat = openai.ChatCompletion.create(model="gpt-4", messages=messages)
    assistant_reply = chat.choices[0].message.content
    
    return jsonify({"response": assistant_reply})

if __name__ == '__main__':
    app.run(debug=True)
