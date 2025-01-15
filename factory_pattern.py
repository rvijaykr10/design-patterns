"""
Usage: Used to create objects dynamically, such as database connections, services, or resources based on runtime conditions.
"""

from fastapi import FastAPI, Depends  # type: ignore


class DatabaseClient:
    def connect(self):
        pass


class PostgresDatabaseClient(DatabaseClient):
    def connect(self):  # type: ignore
        return "Connected to PostgreSQL"


class MongoDatabaseClient(DatabaseClient):
    def connect(self):  # type: ignore
        return "Connected to MongoDB"


class DatabaseFactory:
    def create_client(self, db_type: str) -> DatabaseClient:
        if db_type == "postgres":
            return PostgresDatabaseClient()
        elif db_type == "mongo":
            return MongoDatabaseClient()
        return None  # type: ignore


app = FastAPI()  # type: ignore


def get_db_client(db_type: str = "postgres") -> DatabaseClient:
    factory = DatabaseFactory()
    return factory.create_client(db_type)


@app.get("/db")  # type: ignore
async def get_db(db: DatabaseClient = Depends(get_db_client)):
    return {"message": db.connect()}
