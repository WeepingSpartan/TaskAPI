import random

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates



template=Jinja2Templates(directory="template")


app = FastAPI()

#Display random number
@app.get("/")
def home(request: Request):
    return template.TemplateResponse("home.html",{
        "request": request,
        "somevar": random.randrange(1000000)
    }
)
