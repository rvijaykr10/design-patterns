"""
Usage: Useful for notification systems (e.g., event-driven workflows, user registration notifications, or logging events).
"""

from fastapi import FastAPI
from typing import List


class Observer:
    def update(self, message: str):
        pass


class Logger(Observer):
    def update(self, message: str):
        print(f"Logging message: {message}")


class Notifier(Observer):
    def update(self, message: str):
        print(f"Sending notification: {message}")


class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)


app = FastAPI()


@app.post("/register")
async def register_user():
    subject = Subject()
    subject.add_observer(Logger())
    subject.add_observer(Notifier())
    subject.notify("New user registered!")
    return {"message": "User registered and notifications sent!"}
