import skyscanner
from fastapi import FastAPI, Form
from pydantic import BaseModel

url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
key = 'sh428739766321522266746152871799'

class Item(BaseModel):
    departure: str
    arrival: str
    year: int
    month: int
    day: int

app = FastAPI()

@app.post('/upload/')
def upload(data: Item):
    print(data)
    return data