from proj import patientmanager
from proj.patient import Patient
from proj.doctor import Doctor
from proj.patientmanager import PatientManager
from proj.doctormanager import DoctorManager
from proj.appointment import Appointment
import inspect


p1 = Patient("Ivan", "Martynov", "02.12.2008", "A+", "+380999999999",
             "ivan.martynov@gmail.com", 17)
p2 = Patient("John", "Smith", "01.01.1990", "O-", "+1234567890",
             "john.smith@example.com", 31)
p3 = Patient("Jane", "Doe", "15.05.1985", "B+", "+9876543210",
             "jane.doe@example.com", 36)

print("\t===Patient===\t")
p1.show()
p1.GetAgeCategory()

p2.show()
p2.GetAgeCategory()

p3.show()
p3.GetAgeCategory()
#first_name, last_name, date_of_birth, blood_type, phone, email, full_name, age, is_adult

d1 = Doctor("Ivan", "Martynov", "Cardiologist",
            "LIC-001", "+380999999999", 8, 17)

d2 = Doctor("John", "Doe", "Pediatrician",
            "LIC-002", "+1234567890", 9, 18)

d3 = Doctor("Jane", "Doe", "Dermatologist",
            "LIC-003", "+9876543210", 10, 19)


print("\t===Doctors===\t")
d1.show()

d2.show()

d3.show()

patient_manager = PatientManager()

print ("=== Patient Manager ===")
patient_manager.Add(p1)
patient_manager.Add(p2)
patient_manager.Add(p3)

target = int(input("Enter a target for search:"))
patient_manager.FindById(target).show()

name_for_search = str(input("Enter a name for search:"))
patient_manager.FindByName(name_for_search).show()

id_for_remove = int(input("Enter an ID for removal:"))
patient_manager.Remove(id_for_remove)

patient_manager.Display()

#doctorManager
print("===Doctor Manager===")
doctor_manager = DoctorManager()
doctor_manager.Add(d1)
doctor_manager.Add(d2)
doctor_manager.Add(d3)

doctor_manager.DisplayAll()

speciality_for_search_doctor = str(input("Enter a speciality for search:"))
doctor_manager.FindBySpeciality(speciality_for_search_doctor).show()

id_for_search_doctor = int(input("Enter a id for search:"))
doctor_manager.FindById(id_for_search_doctor).show()

id_for_remove_doctor = int(input("Enter id to delete a doctor: "))
doctor_manager.Remove(id_for_remove_doctor)

doctor_manager.DisplayAll()

appoinment1 = Appointment(p1, d1, "2023-10-01", "10:00")
appoinment2 = Appointment(p2, d2, "2023-10-02", "11:00")
appoinment3 = Appointment(p3, d3, "2023-10-03", "12:00")

print("\t===Appointments===\t")
appoinment1.appointment_show()
appoinment2.appointment_show()
appoinment3.appointment_show()

appoinment1.Cancel("Patient requested cancellation")
appoinment2.Complete()
appoinment3.Cancel("Doctor unavailable")

appoinment1.appointment_show()
appoinment2.appointment_show()
appoinment3.appointment_show()
