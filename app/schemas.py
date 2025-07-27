from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str
    specialization: str
    timings: str

class DoctorOut(DoctorBase):
    id: int
    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int
    date: str
    time: str

class AppointmentOut(AppointmentBase):
    id: int
    class Config:
        from_attributes = True
