"""
Usage: Reduces memory usage by sharing common objects.
"""

from fastapi import FastAPI


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str):
        print(f"LOG: {message}")


app = FastAPI()


@app.get("/log")
async def log_message():
    logger = Logger()
    logger.log("This is a log message")
    return {"message": "Logged successfully"}
