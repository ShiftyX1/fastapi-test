from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from typing import List
from pydantic import BaseModel, Field

from db import base


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")



fake_devices = [
    {"id": 1234, "serial_number": 12345, "name": "Lenovo"},
    {"id": 1221, "serial_number": 12211, "name": "Asus"},
]


class Rank(BaseModel):
    id: int
    name: str
    level_privileges: int = Field(gt=0, le=12)


class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    rank: List[Rank]


class Device(BaseModel):
    id: int
    serial_number: int = Field(ge=0)
    name: str = Field(max_length=10)


@app.post("/device")
def add_device(devices: List[Device]):
    fake_devices.extend(devices)
    return {"status": 200, "data": fake_devices}


@app.get("/list_device/{device_id}", response_model=List[Device])
def get_device(device_id: int):
    return [device for device in fake_devices if device.get("id") == device_id]
