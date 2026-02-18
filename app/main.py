from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
# templatesフォルダを指定
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    # index.htmlにリクエスト情報を渡して表示
    return templates.TemplateResponse("index.html", {"request": request})