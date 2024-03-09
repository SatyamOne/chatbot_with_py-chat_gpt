import os
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_KEY") or 'sk-YOUR API KEY '

# Initialize the messages list with the initial system message
messages = [{"role": "system", "content": "You are a kind helpful assistant."}]

print("Your new assistant is ready!")

# Main loop
while True:
    user_input = input("You: ")  # Take user input
    if user_input == "quit()":  # Check if user wants to quit
        break
    
    # Append user message to the messages list
    messages.append({"role": "user", "content": user_input})
    
    # Get assistant's response from OpenAI's Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Extract assistant's reply from the response
    reply = response["choices"][0]["message"]["content"]
    
    # Append assistant's reply to the messages list
    messages.append({"role": "assistant", "content": reply})
    
    # Print assistant's reply
    print("Assistant:", reply)
