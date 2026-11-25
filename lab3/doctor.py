import datetime

class Doctor:
    _nextId = 0
    Id = 0
    first_name = ""
    last_name = ""
    speciality = ""
    license_number = ""
    phone_number = ""
    work_start_hour = 0
    work_end_hour = 0
    full_name = first_name + " " + last_name
    working_hours = work_end_hour - work_start_hour
    work_schedule = f"{work_start_hour:02d}:00 - {work_end_hour:02d}:00"
    hour = 0
    is_avaiable = False

    def __init__ (self, first_name, last_name, speciality,
                  license_number, phone_number, work_start_hour, work_end_hour):
        self.Id = Doctor._nextId
        Doctor._nextId += 1
        self.first_name = first_name
        self.last_name = last_name
        self.speciality = speciality
        self.license_number = license_number
        self.phone_number = phone_number
        self.work_start_hour = work_start_hour
        self.work_end_hour = work_end_hour

    def can_accept_at(self, hour : int = None) -> bool:
        hour = datetime.datetime.now().hour if hour is None else hour

        if hour >= self.work_start_hour and hour <= self.work_end_hour:
            print("Доступний зараз")
            return True
        else:
            print("Недоступний зараз")
            return False

    def show(self):
        print(f"Doctor ID: {self.Id} | {self.full_name} | {self.speciality} | "
              f"{self.license_number} | {self.phone_number} | {self.can_accept_at()}")
