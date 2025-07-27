from app import models, schemas
from app.database import SessionLocal

def book_appointment(data: schemas.AppointmentBase):
    db = SessionLocal()
    appt = models.Appointment(**data.dict())
    db.add(appt)
    db.commit()
    db.refresh(appt)
    return appt

def get_appointments_by_doctor(doctor_id: int):
    db = SessionLocal()
    return db.query(models.Appointment).filter(models.Appointment.doctor_id == doctor_id).all()

def get_appointments_by_patient(patient_id: int):
    db = SessionLocal()
    return db.query(models.Appointment).filter(models.Appointment.patient_id == patient_id).all()
