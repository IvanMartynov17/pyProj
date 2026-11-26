from proj.patient import Patient

class PatientManager:
    max_patients = 100
    _patients = []
    _count = 0
    count = 0

    def __init__(self):
        _patient = [self.max_patients]
        _count = self.count

    def Add(self, patient):
        if self._count >= self.max_patients:
            print("Error: list is full")
            return
        self._patients.append(patient)
        self._count += 1
        print("Patient added")

    def FindById(self, Id):
        for patient in self._patients:
            if patient.Id == Id:
                return patient
        return None

    def FindByName(self, name):
        for patient in self._patients:
            if patient.FirstName == name:
                print(patient)
                return patient

        return -1

    def Remove(self, id):
        for patient in self._patients:
            if patient.Id == id:
                self._patients.remove(patient)
                self._count -= 1
                print("Patient removed")
                return
        print("Patient not found")

    def Display(self):
        for patient in self._patients:
            patient.show()



