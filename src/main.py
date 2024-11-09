from fastapi import FastAPI
from src.models import Items, Supplier, session

app = FastAPI()

@app.get("/")
async def root():
    return {
        "subject": "Mobile Testing",
        "class": "TI 21 B",
        "purpose": "task for midterm",
        "identity": [
            {
                "name": "Ikrar Bagaskara",
                "nim": "210103101"
            },
            {
                "name": "Anggun Berlian Agustina",
                "nim": "210103178"
            }
        ]
    }


@app.get("/items")
async def get_all_items():
    items_query = session.query(Items)
    return items_query.all()

@app.get("/suppliers")
async def get_all_supplier():
    supplier_query = session.query(Supplier)
    return supplier_query.all()