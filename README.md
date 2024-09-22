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

## Project Structure

```
project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Custom styles
│   └── js/
│       └── script.js      # Frontend JavaScript
├── templates/
│   └── index.html         # Main HTML template
└── music_generator/
    └── generator.py       # Music generation algorithms
```

## How It Works

1. **Mood Selection**: The user selects a mood, which determines the scale and overall feel of the music.
2. **Melody Generation**: A Markov chain model is used to generate a melody based on the selected scale.
3. **Harmony Creation**: Chord progressions are added to complement the melody.
4. **Bass Line**: A bass line is generated to provide a foundation for the composition.
5. **Frontend Rendering**: The application sends the musical data to the frontend, where Tone.js is used to synthesize and play the sounds.

## Customization

You can extend this project in several ways:
- Add more scales and moods
- Implement more complex music generation algorithms
- Introduce different instruments or sound types
- Allow users to save or share their generated music

## Contributing

Contributions to improve the AI Music Generator are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.


