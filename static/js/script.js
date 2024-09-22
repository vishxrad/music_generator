let generatedNotes = null;
let scaleInfo = null;
let tempo = 120;
const synth = new Tone.PolySynth(Tone.Synth).toDestination();
let playing = false;

document.getElementById('generateBtn').addEventListener('click', function() {
    const style = document.getElementById('style').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            style: style
        }),
    })
    .then(response => response.json())
    .then(data => {
        generatedNotes = data.notes;
        scaleInfo = data.scale_info;
        tempo = data.tempo;
        const outputDiv = document.getElementById('musicOutput');
        outputDiv.innerHTML = `
            <h3>Generated ${data.style.charAt(0).toUpperCase() + data.style.slice(1)} Music</h3>
            <p>Scale: ${scaleInfo.name}</p>
            <p>Notes: ${scaleInfo.notes.join(', ')}</p>
            <p>Chord Progression: ${scaleInfo.chord_progression.join(' - ')}</p>
            <p>Tempo: ${tempo} BPM</p>
            <p>Click 'Play Music' to listen.</p>
        `;
        document.getElementById('playBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('playBtn').addEventListener('click', function() {
    if (generatedNotes && !playing) {
        playing = true;
        Tone.start();
        Tone.Transport.bpm.value = tempo;

        const part = new Tone.Part((time, note) => {
            synth.triggerAttackRelease(note.pitch, note.duration, time);
        }, generatedNotes.map((note, index) => [index * 0.5, note])).start(0);

        Tone.Transport.start();

        document.getElementById('playBtn').disabled = true;
        document.getElementById('stopBtn').disabled = false;
    }
});

document.getElementById('stopBtn').addEventListener('click', function() {
    if (playing) {
        Tone.Transport.stop();
        Tone.Transport.cancel();
        playing = false;
        document.getElementById('playBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
    }
});