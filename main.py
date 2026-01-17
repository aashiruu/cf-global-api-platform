import time
import psutil
import logging
from fastapi import FastAPI
from pythonjsonlogger import jsonlogger
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

instrumentator = Instrumentator().instrument(app)

log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)
logger = logging.getLogger("api-logger")
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

@app.on_event("startup")
async def startup_event():
    instrumentator.expose(app)

@app.get("/api/v1/status")
def get_status():
    return {"cpu": psutil.cpu_percent(), "memory": psutil.virtual_memory().percent}

@app.get("/")
def root():
    return {"message": "API is live"}
