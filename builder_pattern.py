"""
Usage: Constructs complex objects step by step.
"""

from fastapi import FastAPI


class ResponseBuilder:
    def __init__(self):
        self.response = {}

    def add_status(self, status: str):
        self.response["status"] = status  # type: ignore
        return self

    def add_message(self, message: str):
        self.response["message"] = message  # type: ignore
        return self

    def add_data(self, data: dict):  # type: ignore
        self.response["data"] = data  # type: ignore
        return self

    def build(self):  # type: ignore
        return self.response  # type: ignore


app = FastAPI()


@app.get("/build-response")
async def build_response():  # type: ignore
    builder = ResponseBuilder()
    response = (  # type: ignore
        builder.add_status("success")
        .add_message("Request was successful")
        .add_data({"item": "value"})  # type: ignore
        .build()
    )
    return response  # type: ignore
