from fastapi import FastAPI
from models import Items, Supplier, session

app = FastAPI()

@app.get("/items")
async def get_all_items():
    items_query = session.query(Items)
    return items_query.all()

@app.get("/suppliers")
async def get_all_supplier():
    supplier_query = session.query(Supplier)
    return supplier_query.all()