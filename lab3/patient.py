import datetime

class Patient:
    next_id = 1
    Id = 0
    FirstName = None
    LastName = None
    DateOfBirth = None
    BloodType = None
    Phone = None
    Email = None
    FullName = None
    Age = 0
    IsAdult = False

    def __init__(self, first_name, last_name, date_of_birth,
                 blood_type, phone, email, age):
        self.Id = Patient.next_id
        Patient.next_id += 1
        self.FirstName = first_name
        self.LastName = last_name
        self.DateOfBirth = date_of_birth
        self.BloodType = blood_type
        self.Phone = phone
        self.Email = email
        self.Age = age


    def GetAgeCategory(self):
        self.FullName = f"{self.FirstName} {self.LastName}"
        if self.Age < 18:
            print (f"{self.FullName} Child")
        elif self.Age > 18 and self.Age < 60:
            print (f"{self.FullName} Adult")
        else:
            print (f"{self.FullName} Pensioner")

    def show(self):
        print(f"ID: [{self.Id}] | {self.FirstName} | {self.LastName} | {self.DateOfBirth} "
              f"| {self.BloodType} | {self.Phone} | {self.Email} | {self.Age} | {self.IsAdult}")
