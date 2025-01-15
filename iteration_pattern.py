"""
Usage: Iterates over a collection without exposing its underlying structure.
"""

from fastapi import FastAPI
from typing import List


class ItemIterator:
    def __init__(self, items: List[str]):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


app = FastAPI()


@app.get("/items")
async def get_items():
    items = ["apple", "banana", "cherry"]
    iterator = ItemIterator(items)
    return {"items": [item for item in iterator]}
