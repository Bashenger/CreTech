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

        # Extend the response data for more diverse interactions
    response_data = {
        "greeting": [
            "Hello there!",
            "Hi!",
            "Greetings!",
            "Hey!",
            "Nice to see you!",
            "Howdy!",
            "Hiya!",
            "Good to see you!"
        ],
        "how_are_you": [
            "I'm doing well, thank you!",
            "I'm good.",
            "I'm fine, how about you?",
            "I'm great!",
            "Feeling good today!",
            "I'm just a program, but I'm functioning perfectly!"
        ],
        "name": [
            "I am a simple chatbot.",
            "You can call me Chatbot.",
            "I don't have a name, really.",
            "I'm just a computer program.",
            "People call me Chatbot.",
            "I go by Chatbot, nice to meet you!"
        ],
        "bye": [
            "Goodbye!",
            "See you later!",
            "Bye bye!",
            "Farewell!",
            "Take care!",
            "Catch you later!",
            "Have a great day!"
        ],
        "thank_you": [
            "You're welcome!",
            "No problem.",
            "Glad I could help!",
            "My pleasure!",
            "You're very welcome.",
            "Anytime!"
        ],
        "help": [
            "I can answer simple questions and have short conversations.",
            "Try saying hello, asking how I am, or saying goodbye.",
            "What do you need help with?",
            "How can I assist you today?",
            "I'm here to help.",
            "Feel free to ask me anything!"
        ],
        "age": [
            "I don't have an age. I'm just a program.",
            "I'm not old, I'm timeless!",
            "Age is just a number, right?",
            "I exist outside of time.",
            "I was created recently.",
            "I don't age like humans do."
        ],
        "created": [
            "I was created using Python.",
            "I was built by a programmer.",
            "I was brought into existence through code.",
            "I am a product of software engineering.",
            "My origins are in programming.",
            "I was designed to assist and chat with you."
        ],
        "favorite_color": [
            "I don't have a favorite color. I perceive information, not color.",
            "As a chatbot, I don't have preferences like favorite colors.",
            "I'm more into data than colors.",
            "I don't process visual information in that way.",
            "I don't have color preferences.",
            "Colors are fascinating, but I don't have a favorite."
        ],
        "joke": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "Why don't eggs tell jokes? They'd crack each other up.",
            "What do you call a fish with no eyes? Fsh!",
            "Why don't they play poker in the jungle? Too many cheetahs!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        "weather": [
            "I'm sorry, I cannot provide real-time weather information.",
            "I don't have access to current weather data.",
            "You can check a weather app or website for that information.",
            "I cannot give you the weather forecast.",
            "For weather details, please consult a weather service.",
            "I wish I could tell you, but I don't have weather data."
        ],
        "time": [
            "I do not have access to the current time.",
            "I cannot tell you the time.",
            "You can check your device for the current time.",
            "I cannot provide time information.",
            "Please check your device for the time.",
            "Time is relative, but I can't tell you the exact time."
        ],
        "hobby": [
            "I don't have hobbies, but I enjoy chatting with you!",
            "I like processing data and learning new things.",
            "My hobby is helping people like you.",
            "I don't have hobbies like humans, but I enjoy being useful."
        ],
        "food": [
            "I don't eat food, but I hear pizza is popular!",
            "I don't have a favorite food, but I can talk about food if you'd like.",
            "I don't eat, but I can help you find recipes!",
            "Food is fascinating, but I don't consume it."
        ],
        "movie": [
            "I don't watch movies, but I hear Inception is great!",
            "I don't have a favorite movie, but I can discuss them with you.",
            "Movies are fun to talk about, even if I can't watch them.",
            "I don't watch movies, but I can recommend some based on reviews."
        ],
        "history": [
            "The Great Wall of China was built over several centuries to protect against invasions.",
            "The first manned moon landing was in 1969 by NASA's Apollo 11 mission.",
            "The Roman Empire was one of the most powerful civilizations in history.",
            "World War II ended in 1945 after six years of conflict.",
            "The Renaissance was a cultural movement that began in Italy in the 14th century."
        ],
        "science": [
            "Water is made up of two hydrogen atoms and one oxygen atom (H2O).",
            "The speed of light is approximately 299,792 kilometers per second.",
            "Albert Einstein developed the theory of relativity.",
            "The human body has 206 bones.",
            "Earth is the third planet from the Sun in our solar system."
        ],
        "geography": [
            "Mount Everest is the tallest mountain in the world, located in the Himalayas.",
            "The Amazon Rainforest is the largest tropical rainforest on Earth.",
            "The Sahara Desert is the largest hot desert in the world.",
            "There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia.",
            "The Nile River is the longest river in the world."
        ],
        "sports": [
            "Soccer, also known as football, is the most popular sport in the world.",
            "The Olympic Games are held every four years and feature athletes from around the globe.",
            "Basketball was invented by James Naismith in 1891.",
            "Cricket is a popular sport in countries like India, Australia, and England.",
            "The FIFA World Cup is the most prestigious soccer tournament."
        ],
        "technology": [
            "The first computer was called the ENIAC and was developed in 1945.",
            "The internet was invented in the late 20th century and revolutionized communication.",
            "Artificial intelligence is a field of computer science focused on creating intelligent machines.",
            "The smartphone was popularized by the release of the iPhone in 2007.",
            "Blockchain technology is the foundation of cryptocurrencies like Bitcoin."
        ],
        "literature": [
            "William Shakespeare is considered one of the greatest playwrights in history.",
            "The novel '1984' by George Orwell explores themes of surveillance and totalitarianism.",
            "J.K. Rowling is the author of the Harry Potter series.",
            "The Iliad and the Odyssey are epic poems attributed to the ancient Greek poet Homer.",
            "The Great Gatsby by F. Scott Fitzgerald is a classic American novel."
        ],
        "default": [
            "I'm not sure I understand.",
            "Could you please rephrase that?",
            "I'm still learning.",
            "I didn't quite get that.",
            "Can you say that again?",
            "I'm sorry, I don't know how to respond to that."
        ]
    }
    
    # Extend the keywords for more intents
    keywords = {
        "greeting": ["hello", "hi", "greetings", "hey", "howdy", "hiya"],
        "how_are_you": ["how are you", "how's it going", "how you doing", "what's up"],
        "name": ["what is your name", "what's your name", "who are you", "your name"],
        "bye": ["bye", "goodbye", "see you later", "farewell", "take care"],
        "thank_you": ["thank you", "thanks", "thank you very much", "appreciate it"],
        "help": ["help", "assistance", "support", "what can you do", "how can you help"],
        "age": ["age", "old are you", "how old"],
        "created": ["created", "made", "built", "who made you", "who created you"],
        "favorite_color": ["favorite color", "what color do you like"],
        "joke": ["joke", "funny", "tell me a joke", "make me laugh"],
        "weather": ["weather", "forecast", "is it raining", "what's the weather"],
        "time": ["time", "clock", "what time is it", "current time"],
        "hobby": ["hobby", "what do you like to do", "pastime"],
        "food": ["food", "favorite food", "what do you eat"],
        "movie": ["movie", "favorite movie", "what movies do you like"],
        "history": ["history", "past", "ancient", "historical", "event"],
        "science": ["science", "physics", "chemistry", "biology", "scientific"],
        "geography": ["geography", "mountain", "river", "continent", "ocean", "desert"],
        "sports": ["sports", "soccer", "football", "basketball", "cricket", "Olympics"],
        "technology": ["technology", "computer", "internet", "AI", "artificial intelligence", "blockchain"],
        "literature": ["literature", "book", "novel", "author", "poem", "Shakespeare"],
        "default": []
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
