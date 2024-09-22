import random
from collections import defaultdict

# Define scales
SCALES = {
    'C_major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'A_minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'G_major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'E_minor': ['E', 'F#', 'G', 'A', 'B', 'C', 'D']
}

# Define common chord progressions
CHORD_PROGRESSIONS = {
    'C_major': ['C', 'G', 'Am', 'F'],
    'A_minor': ['Am', 'F', 'C', 'G'],
    'G_major': ['G', 'Em', 'C', 'D'],
    'E_minor': ['Em', 'C', 'G', 'D']
}

# Define style characteristics
STYLES = {
    'happy': {
        'scales': ['C_major', 'G_major'],
        'tempo_range': (120, 160),
        'note_durations': [0.25, 0.5, 1],
        'melody_range': (4, 6)
    },
    'sad': {
        'scales': ['A_minor', 'E_minor'],
        'tempo_range': (60, 90),
        'note_durations': [1, 1.5, 2],
        'melody_range': (3, 5)
    },
    'epic': {
        'scales': ['C_major', 'G_major'],
        'tempo_range': (90, 110),
        'note_durations': [0.5, 1, 2],
        'melody_range': (3, 6)
    },
    'chill': {
        'scales': ['G_major', 'E_minor'],
        'tempo_range': (70, 100),
        'note_durations': [0.5, 1, 1.5],
        'melody_range': (4, 5)
    }
}

def build_markov_chain(scale, order=2):
    chain = defaultdict(list)
    scale_length = len(scale)

    # Ensure circular transitions
    for i in range(scale_length):
        state = tuple(scale[i:i+order])
        if len(state) == order:  # Ensure the state has the correct number of notes
            next_note = scale[(i+order) % scale_length]  # Circular wrapping
            chain[state].append(next_note)

        # Special case: handle last few states wrapping back to the start
        if i + order >= scale_length:
            wrap_state = tuple(scale[i:] + scale[:(i + order) % scale_length])
            if len(wrap_state) == order:
                next_note = scale[(i + order) % scale_length]
                chain[wrap_state].append(next_note)

    print("Markov chain built:", dict(chain))
    return chain


def generate_melody(chain, length, start=None):
    if start is None:
        start = random.choice(list(chain.keys()))

    melody = list(start)
    print(f"Starting melody with state: {start}")

    for _ in range(length - len(start)):
        state = tuple(melody[-len(start):])
        if state not in chain or not chain[state]:
            print(f"State {state} not found in chain. Using fallback.")
            next_state = random.choice(list(chain.keys()))  # Fallback to a valid state
            next_note = random.choice(chain[next_state])  # Pick the next note from a valid state
        else:
            next_note = random.choice(chain[state])
            print(f"Transitioning from state {state} to {next_note}")
        melody.append(next_note)

    return melody





def generate_chord(scale, melody_note):
    idx = scale.index(melody_note)
    return [scale[idx], scale[(idx+2) % 7], scale[(idx+4) % 7]]

def generate_music(params):
    style = params.get('style', 'happy')
    style_params = STYLES[style]
    
    scale_name = random.choice(style_params['scales'])
    scale = SCALES[scale_name]
    chord_progression = CHORD_PROGRESSIONS[scale_name]
    
    # Build and use Markov chain for melody generation
    markov_chain = build_markov_chain(scale)
    melody_length = 16  # Fixed length, about 4 measures
    melody = generate_melody(markov_chain, melody_length)
    
    # Generate notes with melody and harmony
    notes = []
    for i, note in enumerate(melody):
        # Melody note
        pitch = note + str(random.randint(*style_params['melody_range']))
        duration = random.choice(style_params['note_durations'])
        notes.append({'pitch': pitch, 'duration': duration, 'type': 'melody'})
        
        # Add harmony (chord) every 4 beats
        if i % 4 == 0:
            chord = generate_chord(scale, note)
            for chord_note in chord:
                notes.append({'pitch': chord_note + '3', 'duration': 4, 'type': 'harmony'})
    
    tempo = random.randint(*style_params['tempo_range'])
    
    return notes, scale_name, tempo, style

def get_scale_info(scale_name):
    return {
        'name': scale_name,
        'notes': SCALES[scale_name],
        'chord_progression': CHORD_PROGRESSIONS[scale_name]
    }