from fastapi import FastAPI
from app.routes import payments
from app.logging_config import setup_logging
import os
import uvicorn
import signal
import sys


setup_logging()

app = FastAPI(title="Cloud Native Payments API")


PORT = int(os.getenv("PORT", 8000))

@app.get("/health")
async def health():
    return {"status": "UP"}

@app.get("/ready")
async def readiness():
    # check dependencies if any (DB, API)
    return {"status": "READY"}


def shutdown(sig, frame):
    print("Shutting down gracefully...")
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

app.include_router(payments.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)
