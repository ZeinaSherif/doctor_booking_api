from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import doctor_controller, appointment_controller
from app.database import SessionLocal
from app.models import Doctor

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(doctor_controller.router)
app.include_router(appointment_controller.router)


def seed_doctors():
    db = SessionLocal()
    if db.query(Doctor).count() == 0:  
        sample_doctors = [
            Doctor(name="Dr. Amr Hussein", specialization="Cardiology", timings="9 AM - 1 PM"),
            Doctor(name="Dr. Mariam Youssef", specialization="Dermatology", timings="10 AM - 3 PM"),
            Doctor(name="Dr. Tarek Nabil", specialization="Pediatrics", timings="12 PM - 4 PM"),
        ]
        db.add_all(sample_doctors)
        db.commit()
    db.close()

seed_doctors()
