from google import genai
API_KEY = "YOUR GOOGLE GEMINI API KEY"
try:
    client = genai.Client(api_key=API_KEY)
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        print("Chatbot:", response.text)
except Exception as e:
    print("Error:", e)

#python chatbot.py to run the code.

#you need to install google genai library using pip install google-genai to run the code.   

#Note: The API key used in this code is a placeholder. You need to replace it with your actual API key from Google GenAI to use the chatbot functionality.

# The chatbot will respond to user input until the user types "bye" to exit the conversation.  
