from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/process-audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files['file']
    try:
        # Transcribe the audio using Whisper API
        transcription = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file
        )
        text = transcription.get("text", "")
        return jsonify({"transcription": text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
