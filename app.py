from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/wake", methods=["POST"])
def wake():
    audio = request.files["audio"]
    audio.save("wake.wav")
    result = subprocess.run(["./main", "-m", "models/ggml-base.en.bin", "-f", "wake.wav", "-otxt"], capture_output=True)
    text = open("wake.wav.txt").read()
    return jsonify({"text": text})

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.files["audio"]
    audio.save("input.wav")
    result = subprocess.run(["./main", "-m", "models/ggml-base.en.bin", "-f", "input.wav", "-otxt"], capture_output=True)
    text = open("input.wav.txt").read()
    return jsonify({"text": text})

