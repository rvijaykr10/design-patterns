"""
Usage: Adds behavior to objects dynamically.
"""

from fastapi import FastAPI, Depends  # type: ignore


def check_permissions(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        print("Checking permissions...")
        return func(*args, **kwargs)  # type: ignore

    return wrapper  # type: ignore


app = FastAPI()


@app.get("/secure-endpoint")
@check_permissions
async def secure_endpoint():
    return {"message": "Access granted!"}
