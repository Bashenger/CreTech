# CreTech
This project is part of the CreTech portfolio, a collection of diverse projects showcasing various development skills and approaches to building different types of applications.

# Project 1:
## Simple Chatbot

This is a simple chatbot built using Python and spaCy for natural language processing. The chatbot can respond to greetings, questions, and other simple inputs using predefined responses. It was developed as part of an internship project to demonstrate natural language processing (NLP) capabilities.

## Key Features
- **Predefined Responses**: Responds to greetings, questions, and other simple inputs.
- **Natural Language Processing**: Uses spaCy to process and understand user input.
- **Interactive Chat**: Provides a conversational experience with predefined intents like greetings, jokes, and more.

## Technologies Used

* **Programming Language:** Python
* **NLP Library:** spaCy

## Future Enhancements

This project is continuously being developed. Some planned future features include:

* **Enhanced NLP:** Implement more advanced NLP techniques for better understanding and response generation.
* **Contextual Awareness:** Improve the chatbot's ability to maintain context and remember previous interactions.
* **Expanded Communication Channels:** Integrate with other messaging platforms.
* **User Interface Improvements:** Enhance the user interface for a more engaging experience.
* **Additional Features:** Consider adding features like message editing, deletion, and search.

## Contributing

Contributions to this project are welcome! If you have any ideas, bug reports, or feature requests, please feel free to open an issue or submit a pull request. Please follow standard Git contribution guidelines.


# Project 2:
## Game Development (Tic-Tac-Toe)

This is a classic Tic-Tac-Toe game implemented using Python and the Pygame library.  It features a graphical interface, two-player mode, and a player-versus-computer mode with a simple AI.

## Features

* **Player vs Player Mode:** Supports classic two-player gameplay.
* **Scorecard:** Tracks and displays the score for each player.
* **Graphical Interface:** Uses Pygame for a user-friendly experience.
* **Responsive Design:** Game board adapts to the window size.
* **Enhanced Visuals:** Bold X and O symbols, and a colored background.
* **Game Over Screen:** Displays the winner or a draw message with a "Play Again" button.

## How to Run the Game

1.  **Prerequisites:**
    * Python 3.x
    * Pygame library (`pip install pygame`)

2.  **Installation:**
    * Clone this repository to your local machine.
    * Navigate to the project directory in your terminal.

3.  **Run the Game**

## Game Controls

* Click on an empty cell in the game board to make your move.
* In Player vs Computer mode, the computer will make its move automatically after you.
* After the game ends (win or draw), a "Play Again" button will appear.  Click it to start a new game.

## Future Enhancements

* Implement a more sophisticated AI (e.g., minimax algorithm).
* Add options for different board sizes.
* Implement a settings menu for customizing the game.
* Add sound effects and animations.
## Contributions

Contributions to this project are welcome. If you have any ideas, bug reports, or feature requests,
please feel free to open an issue or submit a pull request. Please follow standard Git contribution guidelines.


# Project 3:

## To Do List App

This is a simple yet effective command-line (CLI) To-Do List application written in Python. It allows users to manage their tasks by adding, viewing, editing, marking as complete/pending, and removing them. The application saves tasks to a local JSON file, ensuring data persistence between sessions. Its straightforward design makes it easy to use and understand, even for beginners.Some of the feature ideas and parts of the code were developed with the assistance of AI.

## Key Features

* **Add Tasks:** Easily add new tasks with a title, an optional description, and an optional due date (DD-MM-YYYY format).
* **View Tasks:**
    * View all tasks.
    * Filter tasks to see only pending ones.
    * Filter tasks to see only completed ones.
* **Mark Task Status:**
    * Mark tasks as completed.
    * Revert completed tasks back to pending.
* **Edit Tasks:** Modify the title, description, or due date of existing tasks.
* **Remove Tasks:** Delete tasks from the list.
* **Data Persistence:** Tasks are automatically saved to a `todolist_data.json` file and loaded when the application starts.
* **User-Friendly CLI:** Interactive menu-driven interface for easy navigation and operation.
* **Date Handling:** Supports due dates and tracks task creation dates.

## Technology Used

* **Python 3:** The core programming language used.
* **Standard Libraries:**
    * `json`: For serializing and deserializing task data to/from a JSON file for persistence.
    * `datetime`: For handling task creation dates and due dates.
    * `os`: For checking file existence (e.g., the tasks data file).

## Future Enhancements

While this application is functional, here are some potential enhancements for the future:

* **Graphical User Interface (GUI):** Develop a GUI using libraries like Tkinter, PyQt, Kivy, or a web-based interface (e.g., using Flask/Django with HTML/CSS/JS) for a more visual experience.
* **Sorting Options:** Allow users to sort tasks by due date, creation date, or title.
* **Search Functionality:** Implement a way to search for tasks by keywords in their title or description.
* **Cloud Sync:** Option to sync tasks with a cloud service (e.g., Google Tasks, or a custom backend).
* **User Accounts:** For multi-user support, if deployed in a shared environment.
* **More Robust Error Handling:** Enhance error handling for edge cases and invalid inputs.
* **Customizable Data Storage:** Allow users to specify a different file path or even choose a database (like SQLite) for storage.
* **Themes/Customization:** (For GUI versions) Allow users to customize the appearance.

## Contributing

Contributions to this project are welcome. If you have any ideas, bug reports, or feature requests,
please feel free to open an issue or submit a pull request. Please follow standard Git contribution guidelines.
