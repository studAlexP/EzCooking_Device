from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

data = "/home/pi/EzCooking/data/data.json"

@app.get("/data")
async def get_json_data():
    return FileResponse(data)