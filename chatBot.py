import openai

openai.api_key = "Your API key goes here!!!"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        break
    
    response = chat_with_gpt(user_input)
    print(f"Chatbot: {response}")

    # This is a change from Fabian via Github Brances