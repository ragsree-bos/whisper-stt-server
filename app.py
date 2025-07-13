from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/wake", methods=["POST"])
def wake():
    audio = request.files["audio"]
    audio.save("wake.wav")
    result = model.transcribe("wake.wav")
    return jsonify({"text": result["text"].strip().lower()})

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.files["audio"]
    audio.save("command.wav")
    result = model.transcribe("command.wav")
    return jsonify({"text": result["text"].strip().lower()})

if __name__ == "__main__":
    app.run()
