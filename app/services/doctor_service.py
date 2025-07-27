from app import models, schemas
from app.database import SessionLocal

def get_all_doctors():
    db = SessionLocal()
    return db.query(models.Doctor).all()

def get_doctor_by_id(doctor_id: int):
    db = SessionLocal()
    doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    db.close()
    return doctor

