from fastapi import FastAPI


class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class NullUser(User):
    def __init__(self):
        super().__init__("Guest")

    def get_name(self):
        return "Guest"


class UserService:
    def __init__(self, user: User = None):  # type: ignore
        self.user = user or NullUser()

    def get_user(self):
        return {"user_name": self.user.get_name()}


app = FastAPI()


@app.get("/user")
async def user_info():
    user_service = UserService()
    return user_service.get_user()
