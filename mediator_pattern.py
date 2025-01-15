"""
Usage: Centralizes communication between objects to reduce direct dependencies.
"""

from fastapi import FastAPI


class Mediator:
    def send_message(self, message: str):
        pass


class EmailService(Mediator):
    def send_message(self, message: str):
        print(f"Sending email with message: {message}")


class SMSService(Mediator):
    def send_message(self, message: str):
        print(f"Sending SMS with message: {message}")


app = FastAPI()


@app.post("/notify")
async def send_notification():
    email_service = EmailService()
    sms_service = SMSService()

    email_service.send_message("Hello via Email!")
    sms_service.send_message("Hello via SMS!")
    return {"message": "Notifications sent"}
