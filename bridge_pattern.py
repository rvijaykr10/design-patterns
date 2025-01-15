"""
Usage: Decouples abstraction from implementation, allowing the two to vary independently.
"""

from fastapi import FastAPI


class DrawingAPI:
    def draw_circle(self, radius):  # type: ignore
        pass


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, radius):  # type: ignore
        return f"Drawing circle with radius {radius} using API1"


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, radius):  # type: ignore
        return f"Drawing circle with radius {radius} using API2"


class Shape:
    def __init__(self, drawing_api: DrawingAPI):
        self.drawing_api = drawing_api

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, drawing_api: DrawingAPI, radius: int):
        super().__init__(drawing_api)
        self.radius = radius

    def draw(self):
        return self.drawing_api.draw_circle(self.radius)  # type: ignore


app = FastAPI()


@app.get("/draw-circle")
async def draw_circle(radius: int, api: int = 1):
    if api == 1:
        drawing_api = DrawingAPI1()
    else:
        drawing_api = DrawingAPI2()

    circle = Circle(drawing_api, radius)
    return {"drawing": circle.draw()}
