"""
Usage: Allows incompatible interfaces to work together by creating an adapter that transforms one interface into another.
"""

from fastapi import FastAPI


# Existing interface
class DatabaseClient:
    def fetch_data(self):
        pass


# New incompatible interface
class MongoDBClient:
    def retrieve(self):
        return "Data from MongoDB"


# Adapter for MongoDBClient to make it compatible with DatabaseClient interface
class MongoDBAdapter(DatabaseClient):
    def __init__(self, mongo_client: MongoDBClient):
        self.mongo_client = mongo_client

    def fetch_data(self):  # type: ignore
        return self.mongo_client.retrieve()


app = FastAPI()


@app.get("/data")
async def get_data():
    mongo_client = MongoDBClient()
    adapted_client = MongoDBAdapter(mongo_client)
    return {"data": adapted_client.fetch_data()}
