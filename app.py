from flask import Flask, request, render_template, redirect, url_for
import os
import whisper
import warnings

app = Flask(__name__)

# Set up folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allow only MP3 files
ALLOWED_EXTENSIONS = {'mp3'}

# Check if file is an allowed type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Initialize Whisper model (use the "base" model for this example)
model = whisper.load_model("base")

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")


@app.route('/')
def index():
    # Render the upload form (index.html)
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if file is part of the request
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    
    # If no file is selected, return error
    if file.filename == '':
        return 'No selected file', 400

    
    # If the file is allowed, process it
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Transcribe the MP3 file using Whisper
        transcription = transcribe_using_whisper(filepath)

        # Redirect to the result page with the transcription
        return render_template('result.html', transcription=transcription)

    # If file type is not allowed
    return 'Invalid file type. Please upload an MP3 file.', 400

def transcribe_using_whisper(audio_filepath):
    # Use Whisper to transcribe the audio file

    result = model.transcribe(audio_filepath)

    return result['text']

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
