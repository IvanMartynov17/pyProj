from proj.patient import Patient
from proj.doctor import Doctor

import datetime

class Appointment:

    _nextId = 1
    def __init__(
            self,
            patient_Id: Patient | int,
            doctor_Id: Doctor | int,
            scheduled_at: datetime.datetime,
            duration_minutes: int,
            status: str = "Scheduled",
            notes: str = ""
    ):
        self.id = Appointment._nextId
        Appointment._nextId += 1
        self.patient_Id = getattr(patient_Id, "Id", patient_Id)
        self.doctor_Id = getattr(doctor_Id, "Id", doctor_Id)
        self.scheduled_at = scheduled_at
        self.duration_minutes = duration_minutes
        self.status = status
        self.notes = notes

    def Cancel(self, reason: str) -> bool:
        if self.status == "Scheduled":
            self.status = "Cancelled"
            print(f"Appointment [{self.id}] cancelled. Reason: {reason}")
            return True
        return False

    def Complete(self) -> bool:
        if self.status == "Scheduled":
            self.status = "Completed"
            print(f"Appointment [{self.id}] completed successfully.")
            return True
        return False

    def appointment_show(self):
        print(f"[{self.id}] | Patient [{self.patient_Id}] -> Doctor [{self.doctor_Id}] | {self.scheduled_at} | Status: {self.status}")

    def __str__(self) -> str:
        return (
            f"[{self.id}] | Patient [{self.patient_Id}] -> Doctor [{self.doctor_Id}] | "
            f"{self.scheduled_at} | Status: {self.status}"
        )
