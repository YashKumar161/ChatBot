# Chatbot using Python NLTK and Flask

## Overview
This project is a simple chatbot built using Python, the Natural Language Toolkit (NLTK), and Flask. The chatbot can understand and respond to user queries in a conversational manner.

## Features
- Natural language understanding using NLTK
- RESTful API using Flask
- Simple and extensible architecture
- Easy to deploy and run locally

## Prerequisites
- Python 3.7 or higher
- Flask
- NLTK

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YashKumar161/chatbot.git
    cd chatbot
    ```

2. Download the necessary NLTK data:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

## Usage
1. Start the Flask server:

    ```bash
    python chatbot.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

## Project Structure
- `chatbot.py`: The main Flask application file, Contains the chatbot logic using NLTK.
- `templates/`: HTML templates for the web interface.
- `static/`: Static files (CSS, JS, images).

## Example
To see the chatbot in action, run the Flask server and visit the local URL. You can then type messages to the chatbot and receive responses.

## Credits
This project was developed by Yash Kumar. For any queries, contact [hello@yashkumar.pro](mailto:hello@yashkumar.pro).
