
# Créer un environnement virtuel
#python -m venv env

# Activer l’environnement
# env\Scripts\activate

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans mon API FastAPI !"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item créé avec succès",  "item": item}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}
