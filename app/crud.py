from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def get_textmodules(db: Session):
    return db.query(models.Textmodule).all()

def get_textmodule(db: Session, module_id: int):
    return db.query(models.Textmodule).filter(models.Textmodule.id == module_id).first()

def create_textmodule(db: Session, module: schemas.TextmoduleCreate):
    existing = db.query(models.Textmodule).filter_by(title=module.title).first()
    if existing:
        raise HTTPException(status_code=400, detail="Title must be unique")
    db_module = models.Textmodule(**module.model_dump())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module

def update_textmodule(db: Session, module_id: int, module_data: schemas.TextmoduleCreate):
    module = db.query(models.Textmodule).filter(models.Textmodule.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Textmodule not found")
    existing = db.query(models.Textmodule).filter(models.Textmodule.title == module_data.title, models.Textmodule.id != module_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Title must be unique")
    module.title = module_data.title
    module.content = module_data.content
    db.commit()
    db.refresh(module)
    return module

def delete_textmodule(db: Session, module_id: int):
    module = db.query(models.Textmodule).filter(models.Textmodule.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Textmodule not found")
    db.delete(module)
    db.commit()
    return module
