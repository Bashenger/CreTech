import spacy
import random

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

def get_response(user_input, conversation_history=None):
    """
    Generates a response to the user's input using spaCy for NLP.

    Args:
        user_input: The text input from the user.
        conversation_history:  A list of previous user and chatbot messages (optional).

    Returns:
        A string containing the chatbot's response.
    """
    # Process the user input with spaCy
    doc = nlp(user_input)

    # Use a dictionary for more structured responses
    response_data = {
        "greeting": [
            "Hello there!",
            "Hi!",
            "Greetings!",
            "Hey!",
            "Nice to see you!"
        ],
        "how_are_you": [
            "I'm doing well, thank you!",
            "I'm good.",
            "I'm fine, how about you?",
            "I'm great!",
            "Feeling good today!"
        ],
        "name": [
            "I am a simple chatbot.",
            "You can call me Chatbot.",
            "I don't have a name, really.",
            "I'm just a computer program.",
            "People call me Chatbot."
        ],
        "bye": [
            "Goodbye!",
            "See you later!",
            "Bye bye!",
            "Farewell!",
            "Take care!"
        ],
        "thank_you": [
            "You're welcome!",
            "No problem.",
            "Glad I could help!",
            "My pleasure!",
            "You're very welcome."
        ],
        "help": [
            "I can answer simple questions and have short conversations.",
            "Try saying hello, asking how I am, or saying goodbye.",
            "What do you need help with?",
            "How can I assist you today?",
            "I'm here to help."
        ],
        "age": [
            "I don't have an age. I'm just a program.",
            "I'm not old, I'm timeless!",
            "Age is just a number, right?",
            "I exist outside of time.",
            "I was created recently."
        ],
        "created": [
            "I was created using Python.",
            "I was built by a programmer.",
            "I was brought into existence through code.",
            "I am a product of software engineering.",
            "My origins are in programming."
        ],
        "favorite_color": [
            "I don't have a favorite color. I perceive information, not color.",
            "As a chatbot, I don't have preferences like favorite colors.",
            "I'm more into data than colors.",
            "I don't process visual information in that way.",
            "I don't have color preferences."
        ],
        "joke": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "Why don't eggs tell jokes? They'd crack each other up.",
            "What do you call a fish with no eyes? Fsh!",
            "Why don't they play poker in the jungle? Too many cheetahs!"
        ],
        "weather": [
            "I'm sorry, I cannot provide real-time weather information.",
            "I don't have access to current weather data.",
            "You can check a weather app or website for that information.",
            "I cannot give you the weather forecast.",
            "For weather details, please consult a weather service."
        ],
        "time": [
            "I do not have access to the current time.",
            "I cannot tell you the time.",
            "You can check your device for the current time.",
            "I cannot provide time information.",
            "Please check your device for the time."
        ],
        "default": [
            "I'm not sure I understand.",
            "Could you please rephrase that?",
            "I'm still learning.",
            "I didn't quite get that.",
            "Can you say that again?"
        ]
    }

    # Keywords and intents (using spaCy's terms)
    keywords = {
        "greeting": ["hello", "hi", "greetings", "hey"],
        "how_are_you": ["how are you", "how's it going", "how you doing"],
        "name": ["what is your name", "what's your name", "who are you"],
        "bye": ["bye", "goodbye", "see you later", "farewell"],
        "thank_you": ["thank you", "thanks", "thank you very much"],
        "help": ["help", "assistance", "support", "what can you do"],
        "age": ["age", "old are you"],
        "created": ["created", "made", "built"],
        "favorite_color": ["favorite color"],
        "joke": ["joke", "funny"],
        "weather": ["weather", "forecast"],
        "time": ["time", "clock"]
    }

     # Check for keywords using spaCy
    intent = "default"  # Default intent
    for key, words in keywords.items():
        for word in words:
            if word in doc.text.lower():
                intent = key
                break
        if intent != "default":
            break

    # Enhanced context handling (very basic)
    if conversation_history:
        if "what is your name" in user_input.lower() and "Chatbot" in conversation_history[-1].lower():
            return "I've already told you, I'm Chatbot!"

    # Select a response based on the intent
    if intent in response_data:
        response = random.choice(response_data[intent])
    else:
        response = random.choice(response_data["default"])

    return response

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Enhanced Chatbot!")
    print("You can type 'bye' to exit.")

    conversation_history = []  # List to store conversation history

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input, conversation_history)
            print("Chatbot:", response)
            conversation_history.append("You: " + user_input)
            conversation_history.append("Chatbot: " + response)

if __name__ == "__main__":
    main()
