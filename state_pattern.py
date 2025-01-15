"""
Usage: Allows an object to change its behavior when its internal state changes.
"""

from fastapi import FastAPI


class State:
    def do_action(self, context):  # type: ignore
        pass


class ConcreteStateA(State):
    def do_action(self, context):  # type: ignore
        context.state = ConcreteStateB()
        return "State A, transitioning to State B"


class ConcreteStateB(State):
    def do_action(self, context):  # type: ignore
        context.state = ConcreteStateA()
        return "State B, transitioning to State A"


class Context:
    def __init__(self):
        self.state = ConcreteStateA()

    def request(self):
        return self.state.do_action(self)  # type: ignore


app = FastAPI()


@app.get("/state")
async def state_machine():
    context = Context()
    first_action = context.request()
    second_action = context.request()
    return {"first_action": first_action, "second_action": second_action}
