from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="build/static"), name="static")
templates = Jinja2Templates(directory="build")

@app.get("/api") # use seperate application mount and proxy with nginx
async def root():
    return {"message": "Hello World"}

@app.get("/{full_path:path}")
async def serve_spa(request: Request, full_path: str):
    print("full_path: "+full_path)
    return templates.TemplateResponse("index.html", {"request": request})