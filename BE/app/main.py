from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, database, schemas, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/textmodules/", response_model=list[schemas.TextmoduleOut])
def read_all(db: Session = Depends(database.get_db)):
    return crud.get_textmodules(db)

@app.get("/textmodules/{module_id}", response_model=schemas.TextmoduleOut)
def read_one(module_id: int, db: Session = Depends(database.get_db)):
    module = crud.get_textmodule(db, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Textmodule not found")
    return module

@app.post("/textmodules/", response_model=schemas.TextmoduleOut)
def create(module: schemas.TextmoduleCreate, db: Session = Depends(database.get_db)):
    return crud.create_textmodule(db, module)

@app.put("/textmodules/{module_id}", response_model=schemas.TextmoduleOut)
def update(module_id: int, module_data: schemas.TextmoduleCreate, db: Session = Depends(database.get_db)):
    return crud.update_textmodule(db, module_id, module_data)

@app.delete("/textmodules/{module_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(module_id: int, db: Session = Depends(database.get_db)):
    crud.delete_textmodule(db, module_id)
    return
