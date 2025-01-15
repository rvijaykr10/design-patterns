"""
Usage: Captures and externalizes an object's internal state so that it can be restored later without violating encapsulation.
"""

from fastapi import FastAPI


class Memento:
    def __init__(self, state):  # type: ignore
        self.state = state


class Originator:
    def __init__(self):
        self.state = ""

    def set_state(self, state):  # type: ignore
        self.state = state  # type: ignore

    def save_state(self):
        return Memento(self.state)  # type: ignore

    def restore_state(self, memento: Memento):
        self.state = memento.state


class Caretaker:
    def __init__(self):
        self.memento = None

    def save(self, memento: Memento):
        self.memento = memento

    def restore(self):
        return self.memento


app = FastAPI()


@app.get("/memento")
async def memento():  # type: ignore
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("State 1")  # type: ignore
    caretaker.save(originator.save_state())

    originator.set_state("State 2")  # type: ignore

    originator.restore_state(caretaker.restore())  # type: ignore

    return {"restored_state": originator.state}  # type: ignore
