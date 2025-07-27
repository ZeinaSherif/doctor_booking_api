from fastapi import APIRouter, HTTPException
from app.schemas import AppointmentBase, AppointmentOut
from app.services import appointment_service
from typing import List
from app.services import doctor_service

router = APIRouter()

@router.post("/appointments", response_model=AppointmentOut)
def book_appt(appt: AppointmentBase):
    doctor = doctor_service.get_doctor_by_id(appt.doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    patient = appointment_service.get_patient_by_id(appt.patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return appointment_service.book_appointment(appt)



@router.get("/appointments", response_model=List[AppointmentOut])
def get_appts(doctor_id: int = None, patient_id: int = None):
    if doctor_id:
        return appointment_service.get_appointments_by_doctor(doctor_id)
    elif patient_id:
        return appointment_service.get_appointments_by_patient(patient_id)
    return []
