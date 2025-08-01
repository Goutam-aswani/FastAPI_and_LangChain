from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
 
class Item(BaseModel):
    name : str
    price : float
    is_offer : Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name":item.name,"item_price" : item.price, "item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


