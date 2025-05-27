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

# Project 4:

## Weather API Application

A command-line Python application to fetch and display current weather and 5-day forecasts for any city or coordinates using the OpenWeatherMap API.

## Features

- Get current weather by city name or geographic coordinates (latitude & longitude)
- Display 5-day weather forecast (with temperature, humidity, wind speed, and description)
- Supports metric, imperial, and standard units
- User-friendly CLI interface

## Requirements

- Python 3.7+
- `requests` library

Install dependencies with:

```
pip install -r requirements.txt
```

## Setup

1. **Get an API Key:**  
   Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get your free API key.

2. **Configure the API Key:**  
   Open `Weather API.py` and replace the value of `YOUR_API_KEY` with your actual API key:

   ```python
   YOUR_API_KEY = 'your_actual_api_key_here'
   ```

## Usage

Run the application:

```
python "Weather API.py"
```

Follow the prompts to:
- Enter a city name or coordinates
- View current weather and optionally a 5-day forecast

## Example

```
--- Weather Forecast Application ---
Choose an option:
1. Get weather by City Name
2. Get weather by Coordinates (Latitude & Longitude)
3. Exit
Enter your choice (1, 2, or 3): 1
Enter city name: Delhi

--- Current Weather ---
Location: Delhi, IN
Temperature: 34°C (Feels like: 36°C)
Description: Clear sky
Humidity: 40%
Pressure: 1005 hPa
Wind Speed: 2.1 m/s
Sunrise: 05:23:45
Sunset: 19:12:10
```

## Notes

- If you see an "Invalid API key" error, double-check your API key and ensure it is active.
- The application uses the free tier of OpenWeatherMap, which may have request limits.

## Future Enhancements

- **GUI Support:** Add a graphical user interface for easier interaction.
- **Weather Alerts:** Integrate weather alerts and warnings from the API.
- **Historical Data:** Allow users to fetch historical weather data.
- **Unit Selection:** Enable users to choose units (metric, imperial, standard) at runtime.
- **Location Detection:** Auto-detect user location for weather queries.
- **Error Logging:** Implement advanced error logging and reporting.
- **API Key Management:** Securely manage and store API keys.
- **Export Data:** Allow exporting weather data to CSV or JSON files.
- **Testing:** Add automated unit and integration tests.
- **Dockerization:** Provide a Dockerfile for easy deployment.

## Contributing

Contributions to this project are welcome. If you have any ideas, bug reports, or feature requests,
please feel free to open an issue or submit a pull request. Please follow standard Git contribution guidelines.
