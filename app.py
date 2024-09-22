from flask import Flask, render_template, request, jsonify
from music_generator.generator import generate_music, get_scale_info, STYLES

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', styles=list(STYLES.keys()))

@app.route('/generate', methods=['POST'])
def generate():
    params = request.json
    notes, scale_name, tempo, style = generate_music(params)
    scale_info = get_scale_info(scale_name)
    return jsonify({'notes': notes, 'scale_info': scale_info, 'tempo': tempo, 'style': style})

if __name__ == '__main__':
    app.run(debug=True)