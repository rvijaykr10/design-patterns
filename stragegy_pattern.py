"""
Usage: Helps to select and switch between different strategies, like validation methods or processing algorithms, based on input or user preference.
"""

from fastapi import FastAPI
from typing import Callable  # type: ignore


class Strategy:
    def execute(self, data: str) -> str:  # type: ignore
        pass


class UpperCaseStrategy(Strategy):
    def execute(self, data: str) -> str:
        return data.upper()


class LowerCaseStrategy(Strategy):
    def execute(self, data: str) -> str:
        return data.lower()


class TextProcessor:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def process(self, data: str) -> str:
        return self.strategy.execute(data)


app = FastAPI()


@app.get("/process-text")
async def process_text(text: str, strategy: str = "upper"):
    if strategy == "upper":
        processor = TextProcessor(UpperCaseStrategy())
    else:
        processor = TextProcessor(LowerCaseStrategy())
    return {"processed_text": processor.process(text)}


app = FastAPI()


@app.post("/validate")
async def validate_data(data: dict):  # type: ignore
    validator = Validator(JSONValidationStrategy())  # type: ignore
    if validator.validate(data):  # type: ignore
        return {"message": "Valid JSON"}
    else:
        validator.set_strategy(XMLValidationStrategy())  # type: ignore
        if validator.validate(data):  # type: ignore
            return {"message": "Valid XML"}
        return {"message": "Invalid data"}
