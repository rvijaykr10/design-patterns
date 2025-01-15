"""
Usage: Encapsulates a request as an object.
"""

from fastapi import FastAPI


class Command:
    def execute(self):
        pass


class CreateUserCommand(Command):
    def execute(self):  # type: ignore
        return "Creating new user"


class DeleteUserCommand(Command):
    def execute(self):  # type: ignore
        return "Deleting user"


class CommandInvoker:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def execute_command(self):
        return self.command.execute()  # type: ignore


app = FastAPI()


@app.post("/user/create")
async def create_user():
    invoker = CommandInvoker()
    invoker.set_command(CreateUserCommand())
    return {"message": invoker.execute_command()}


@app.delete("/user/delete")
async def delete_user():
    invoker = CommandInvoker()
    invoker.set_command(DeleteUserCommand())
    return {"message": invoker.execute_command()}
