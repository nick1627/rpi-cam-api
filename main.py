from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from mockCamera import MockCamera
from storage import Storage
from datetime import datetime

try:
    from picamera2 import Picamera2
    picam = Picamera2()
except ImportError:
    picam = MockCamera()

app = FastAPI()
storage = Storage()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/imageNames")
def get_image_names():
    return storage.list() 

@app.get("/images/{image_id}")
def get_image(image_id: str):
    imagePath = storage.get(image_id)
    return FileResponse(imagePath)

@app.get("/images/latest")
def get_latest_image(): # todo do this next
    names = storage.list()
    latest = max(names, key=lambda p: p.name)
    return FileResponse(latest)

@app.post("/capture")
async def take_picture():
    now = datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')
    filename = "%s.jpg" % now
    await picam.start_and_capture_file(filename)

@app.delete("/images/{image_id}")
def delete_image(image_id: str):
    storage.delete(image_id)
