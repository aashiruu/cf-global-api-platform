import time
import psutil
import platform
import logging
from fastapi import FastAPI, Request
from pythonjsonlogger import jsonlogger
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Aashiruu Global API")

# Setup Logging
log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)
logger = logging.getLogger("api-logger")
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# Prometheus (This is what Grafana sees)
Instrumentator().instrument(app).expose(app)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info("request", extra={
        "method": request.method, 
        "path": request.url.path, 
        "status": response.status_code,
        "duration_ms": round(duration * 1000, 2)
    })
    return response

@app.get("/")
def read_root():
    return {"message": "API is live", "version": "1.1.0"}

@app.get("/api/v1/status")
def get_status():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "uptime": round(psutil.boot_time(), 2)
    }
