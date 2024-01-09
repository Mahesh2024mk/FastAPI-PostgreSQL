from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import schemas
import models
import database

app = FastAPI()

# Initialize the database
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(user: schemas.myUser, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
