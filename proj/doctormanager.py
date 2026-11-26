from proj import doctor
from proj.doctor import Doctor

class DoctorManager:
    max_doctors = 50
    _doctor = [max_doctors]
    _count = 0
    count = _count

    def __init__(self):
        self._doctor = []
        self._count = 0

    def Add(self, doctor):
        if self.count < self.max_doctors:
            self._doctor.append(doctor)
            self._count += 1
            print("Doctor added successfully")
        else:
            print("Error: Doctor list is full")
        return

    def FindById(self, Id):
        for doctor in self._doctor:
            if doctor.Id == Id:
                return doctor
        return None


    def FindBySpeciality(self, speciality):
        for doctor in self._doctor:
            if doctor.speciality == speciality:
                return doctor
        return None

    def GetAll(self):
        return self._doctor

    def Remove(self, Id):
        for doctor in self._doctor:
            if doctor.Id == Id:
                self._doctor.remove(doctor)
                self._count -= 1
                print("Doctor removed successfully")
                return
        print("Error: Doctor not found")

    def DisplayAll(self):
        for doctor in self._doctor:
            print(doctor)