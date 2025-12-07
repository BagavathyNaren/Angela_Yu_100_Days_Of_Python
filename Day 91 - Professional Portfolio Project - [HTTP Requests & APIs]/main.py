from flask import Flask, render_template, request, redirect, url_for, flash, redirect, url_for, session, send_file
from PyPDF2 import PdfReader
from gtts import gTTS
import uuid
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'

# Get the absolute path of the directory where main.py is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Join it with your upload folder name
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')


# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    audio_file_path = request.args.get('filename', '')
    if request.method == 'POST':
        file = request.files['filename']
        if file:
            # Ensure the upload folder exists before saving the file
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            session['file_path'] = file_path
            text_to_convert = extract_text_from_pdf(file_path)
            session['text_to_convert'] = text_to_convert
            flash("File uploaded and text extracted successfully")
            return render_template("index.html",
                                   text_to_convert=text_to_convert,
                                   audio_file_path=audio_file_path) 
    return render_template("index.html",
                           text_to_convert=session.get('text_to_convert', ''),
                           audio_file_path=audio_file_path)


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    all_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text += text
    return all_text


@app.route("/convert_audio", methods=["GET"])
def convert_and_save_audio():
    text_to_convert = session.get('text_to_convert', '')
    if text_to_convert:
        cleaned_text = " ".join(text_to_convert.split())
        text_to_speech = gTTS(cleaned_text)

        # Generate a unique name like 'a1b2c3d4-....mp3'
        unique_filename = f"{uuid.uuid4()}.mp3" 
        audio_file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)

        text_to_speech.save(audio_file_path)
        session['audio_file_path'] = unique_filename  # Store audio file path
        flash(f"Audio saved successfully as {audio_file_path}")
        return redirect(url_for('home', filename=unique_filename))
    else:
        flash("No text available for conversion")
        return redirect(url_for('home'))



@app.route("/audio/<filename>")
def get_audio(filename):
    return send_file(
        os.path.join(app.config['UPLOAD_FOLDER'], filename),
        mimetype="audio/mpeg",
        as_attachment=False
    )

if __name__ == '__main__':
    app.run(debug=True)