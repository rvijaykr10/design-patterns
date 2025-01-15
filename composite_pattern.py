"""
Usage: Composes objects into tree-like structures for part-whole hierarchies.
"""

from fastapi import FastAPI
from typing import List


class Component:
    def operation(self):
        pass


class Item(Component):
    def __init__(self, name: str):
        self.name = name

    def operation(self):  # type: ignore
        return f"Item: {self.name}"


class Cart(Component):
    def __init__(self):
        self.items: List[Component] = []

    def add(self, component: Component):
        self.items.append(component)

    def operation(self):  # type: ignore
        return [item.operation() for item in self.items]


app = FastAPI()


@app.get("/cart")
async def get_cart():
    cart = Cart()
    cart.add(Item("Laptop"))
    cart.add(Item("Phone"))
    return {"cart": cart.operation()}
