from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from db import base


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")



