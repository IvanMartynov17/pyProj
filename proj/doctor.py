import datetime
import inspect

class Doctor:

    _nextId = 1
    def __init__ (
            self, 
            first_name: str,
            last_name: str, 
            speciality: str,
            license_number: str, 
            phone_number: str, 
            work_start_hour: int, 
            work_end_hour: int
    ):
        self.Id = Doctor._nextId
        Doctor._nextId += 1
        self.first_name = first_name
        self.last_name = last_name
        self.speciality = speciality
        self.license_number = license_number
        self.phone_number = phone_number
        self.work_start_hour = work_start_hour
        self.work_end_hour = work_end_hour

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def working_hours(self):
        return f"{self.work_start_hour}:00 - {self.work_end_hour}:00"

    @property
    def work_schedule(self) -> str:
        return f"{self.work_start_hour:02d}:00 - {self.work_end_hour:02d}:00"
    
    def can_accept_at(self, hour : int | None = None) -> bool:
        hour = datetime.datetime.now().hour if hour is None else hour
        return self.work_start_hour <= hour <= self.work_end_hour

    def format_info(self) -> str:
        status = "Доступний зараз" if self.can_accept_at() else "Недоступний зараз"
        return (
            f"Doctor ID: {self.Id} | {self.full_name} | {self.speciality} | "
            f"Ліцензія: {self.license_number} | Тел.: {self.phone_number} | "
            f"Графік: {self.work_schedule} ({self.working_hours} год) | {status}"
        )

    def show(self):
        print(self.format_info())

    def __str__(self) -> str:
        return self.format_info()
    
