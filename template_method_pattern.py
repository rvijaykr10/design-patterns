"""
Usage: Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
"""

from fastapi import FastAPI


class DataProcessor:
    def process(self):
        self.load_data()
        self.clean_data()
        self.analyze_data()

    def load_data(self):
        pass

    def clean_data(self):
        pass

    def analyze_data(self):
        pass


class ConcreteDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading data from file...")

    def clean_data(self):
        print("Cleaning data...")

    def analyze_data(self):
        print("Analyzing data...")


app = FastAPI()


@app.get("/process")
async def process_data():
    processor = ConcreteDataProcessor()
    processor.process()
    return {"message": "Data processed"}
