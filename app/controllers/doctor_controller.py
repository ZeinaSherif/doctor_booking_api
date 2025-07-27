from fastapi import APIRouter, HTTPException
from app.services import doctor_service
from app.schemas import DoctorOut
from typing import List
router = APIRouter()

@router.get("/doctors", response_model=List[DoctorOut])
def list_doctors():
    return doctor_service.get_all_doctors()

@router.get("/doctors/{doctor_id}", response_model=DoctorOut)
def get_doctor(doctor_id: int):
    doctor = doctor_service.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
