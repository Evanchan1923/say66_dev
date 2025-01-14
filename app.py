from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# List of random responses
RESPONSES = [
    "That's interesting!",
    "Could you tell me more?",
    "I didn't see that coming!",
    "Wow, really?",
    "Let me think about that...",
    "That's a great point!"
]

@app.route("/api/respond", methods=["POST"])
def respond():
    """Endpoint to handle text or audio input and return a random response."""
    if "text" in request.json:
        input_text = request.json["text"]
        response = random.choice(RESPONSES)
        return jsonify({"input": input_text, "response": response})
    elif "audio" in request.files:
        audio_file = request.files["audio"]
        # Here you can process the audio file if needed
        response = random.choice(RESPONSES)
        return jsonify({"input": "audio file received", "response": response})
    else:
        return jsonify({"error": "Invalid input. Provide 'text' or 'audio'."}), 400

@app.route("/", methods=["GET"])
def home():
    """Simple home route."""
    return "Welcome to the Random Response API! Use /api/respond to interact."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
