from fastapi import FastAPI, Form, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Template
import random


# 初始化 FastAPI 应用
app = FastAPI()

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 定义响应数据
RESPONSES = [
    "That's interesting!",
    "Could you tell me more?",
    "I didn't see that coming!",
    "Wow, really?",
    "Let me think about that...",
    "That's a great point!"
]

# 首页路由
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html") as f:
        template = Template(f.read())
    return HTMLResponse(template.render())

# API 路由 - POST 请求
@app.post("/api/respond")
async def respond(request: Request, text: str = Form(None), audio: UploadFile = None):
    # 打印收到的请求体内容
    form = await request.form()
    form_data = {key: value for key, value in form.items()}
    print("Form data received:", form_data)

    if text:
        response = random.choice(RESPONSES)
        return JSONResponse({"input": text, "response": response})
    elif audio:
        response = random.choice(RESPONSES)
        return JSONResponse({"input": "audio file received", "response": response})
    else:
        return JSONResponse(
            {"error": "Invalid input. Provide 'text' in form data or 'audio' as a file."},
            status_code=400,
        )