
from fastapi import FastAPI, Depends
import models
from database import Base, SessionLocal, engine
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)
# create function to give us access to database 
def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close_all()


app = FastAPI()


@app.get("/")
def getItems(db: Session = Depends(get_db)):
    items = db.query(models.MemoryItem).all()
    return items


@app.get("/{n}")
async def get_last_data(n: int, db: Session = Depends(get_db)):
    items = db.query(models.MemoryItem).all()
    if n <= 0 or n > len(items):
        return (f"Invalid value for 'n'. Please provide a value between 0 and {len(items)}")
    last_n_items = items[-n:]
    return last_n_items
