"""
Usage: Provides a surrogate or placeholder to control access to an object, often used for lazy loading or access control.
"""

from fastapi import FastAPI


class RealService:
    def perform_task(self):
        return "Task performed by RealService"


class ProxyService:
    def __init__(self, real_service: RealService):
        self.real_service = real_service

    def perform_task(self):
        print("ProxyService: Performing some checks before real service call")
        return self.real_service.perform_task()


app = FastAPI()


@app.get("/task")
async def perform_task():
    real_service = RealService()
    proxy = ProxyService(real_service)
    return {"message": proxy.perform_task()}
