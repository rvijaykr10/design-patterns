"""
Usage: Ensures a single instance of a class, useful for managing global objects like database connections, configuration managers, and caches.
"""

from fastapi import FastAPI  # type: ignore


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str):
        print(f"LOG: {message}")


app = FastAPI()  # type: ignore


@app.get("/log")  # type: ignore
async def log_message():
    logger = Logger()
    logger.log("This is a log message")
    return {"message": "Logged successfully"}
