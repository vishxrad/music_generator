# AI Music Generator

## Overview

The AI Music Generator is an interactive web application that uses artificial intelligence techniques to create unique musical compositions. By leveraging Markov chains and music theory principles, this application generates melodies, harmonies, and bass lines that can be played directly in the browser.

## Features

- **Mood-based Music Generation**: Users can select a mood (happy, sad, relaxed, or mysterious) to influence the musical output.
- **Dynamic Melody Creation**: Utilizes Markov chains to generate coherent and interesting melodies.
- **Harmonic Accompaniment**: Automatically generates chord progressions to accompany the melody.
- **Bass Line Generation**: Creates a complementary bass line to add depth to the composition.
- **Real-time Playback**: Allows users to listen to the generated music directly in their web browser.
- **Music Theory Integration**: Incorporates scale and chord progression concepts for musically sound output.

## Technologies Used

- Backend: Python, Flask
- Frontend: HTML, CSS (Bootstrap), JavaScript
- Music Generation: Custom Python algorithms
- Audio Playback: Tone.js library

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-music-generator.git
   cd ai-music-generator
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://127.0.0.1:5000`

## Usage

1. On the main page, you'll see a mood selector and a "Generate Music" button.
2. Choose a mood from the dropdown menu.
3. Click "Generate Music" to create a new composition.
4. Once the music is generated, you'll see information about the scale and chord progression used.
5. Click "Play Music" to listen to your generated composition.
6. Use the "Stop Music" button to end playback at any time.

# AI Music Generator

[Previous sections remain unchanged]

## Project Structure and File Descriptions

```
project/
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
└── music_generator/
    └── generator.py
```

### File Descriptions

#### `app.py`
This is the main Flask application file. It serves as the entry point for the web application and handles routing and request processing. Key functionalities include:
- Setting up the Flask application
- Defining routes for the home page and music generation API
- Handling requests and responses between the frontend and the music generation backend

#### `requirements.txt`
This file lists all the Python dependencies required to run the project. It typically includes:
- Flask
- Any additional libraries used in the music generation process

#### `static/css/style.css`
This CSS file contains custom styles for the web application. It defines the visual appearance of elements such as:
- Layout of the page
- Styling for buttons and input fields
- Design of the music playback interface

#### `static/js/script.js`
This JavaScript file handles client-side interactions and functionality. Its responsibilities include:
- Sending requests to the server for music generation
- Handling the playback of generated music using Tone.js
- Updating the UI based on user interactions and server responses

#### `templates/index.html`
This is the main (and only) HTML template for the application. It defines the structure of the web page, including:
- The layout of the controls (mood selector, generate button, etc.)
- Placeholders for displaying information about the generated music
- Links to the CSS and JavaScript files

#### `music_generator/generator.py`
This is the core of the music generation system. It contains the algorithms and logic for creating music. Key components include:
- Definitions of scales and chord progressions
- Implementation of the Markov chain for melody generation
- Functions for generating chords and bass lines
- The main `generate_music` function that orchestrates the entire music creation process

### How These Files Work Together

1. When a user accesses the application, Flask (`app.py`) serves the `index.html` template.
2. The user interacts with the page, which triggers JavaScript functions in `script.js`.
3. When music generation is requested, `script.js` sends an AJAX request to the server.
4. `app.py` receives this request and calls functions from `generator.py`.
5. `generator.py` creates the musical elements and returns them to `app.py`.
6. `app.py` sends this data back to the client-side JavaScript.
7. `script.js` then uses Tone.js to play the generated music and updates the UI.
8. Throughout this process, `style.css` ensures that the application looks visually appealing.



