from flask import Flask, request, jsonify, render_template
import random
from flask_cors import CORS

# 初始化 Flask 应用
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Enable CORS for all routes

# 定义响应数据
RESPONSES = [
    "That's interesting!",
    "Could you tell me more?",
    "I didn't see that coming!",
    "Wow, really?",
    "Let me think about that...",
    "That's a great point!"
]

# API 路由 - POST 请求
@app.route("/api/respond", methods=["POST"])
def respond():
    if request.is_json and "text" in request.json:
        input_text = request.json["text"]
        response = random.choice(RESPONSES)
        return jsonify({"input": input_text, "response": response})
    elif "audio" in request.files:
        audio_file = request.files["audio"]
        response = random.choice(RESPONSES)
        return jsonify({"input": "audio file received", "response": response})
    else:
        return jsonify({"error": "Invalid input. Provide 'text' in JSON or 'audio' as a file."}), 400

# 首页路由 - GET 请求
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# 入口点，供 uvicorn 使用
def create_app():
    return app
