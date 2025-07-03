from flask import Flask, request, render_template, redirect, url_for
import os
import whisper
import warnings

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'mp3'}

# input validation for files
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# for better results, please select large or medium (tiny, base, small, medium, large, turbo (not recommended for translating non-english tasks))
model = whisper.load_model("small")

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")


@app.route('/')
def index():
    # upload form
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # file validation
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    
    # more file validation
    if file.filename == '':
        return 'No selected file', 400

    
    # passed all validation checks
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename) # for upload folder
        file.save(filepath)

        transcription = transcribe_using_whisper(filepath)

        # returns result.html
        return render_template('result.html', transcription=transcription)

    # file validation
    return 'Invalid file type. Please upload an MP3 file.', 400

def transcribe_using_whisper(audio_filepath):

    result = model.transcribe(audio_filepath)

    segments = result['segments']
    
    # iterate through to identify start and end segments
    lines = []
    for segment in segments:
        start = segment['start']
        end = segment['end']
        text = segment['text'].strip()
        lines.append(f"[{start:.2f} - {end:.2f}] {text}")

    return '\n\n'.join(lines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

''' when running locally, please reference:
if __name__ == '__main__':
    app.run(debug=True)
'''
