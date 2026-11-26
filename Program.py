from proj import patientmanager
from proj.patient import Patient
from proj.doctor import Doctor
from proj.patientmanager import PatientManager
from proj.doctormanager import DoctorManager

p1 = Patient("Martynov", "Ivan", "02.12.2008", "A+", "+380999999999",
             "ivan.martynov@gmail.com", 17)
p2 = Patient("Smith", "John", "01.01.1990", "O-", "+1234567890",
             "john.smith@example.com", 31)
p3 = Patient("Doe", "Jane", "15.05.1985", "B+", "+9876543210",
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

id_for_search_doctor = str(input("Enter a name for search:"))
doctor_manager.FindByName(id_for_search_doctor).show()

id_for_remove_doctor = int(input("Enter id to delete a doctor: "))
doctor_manager.Remove(id_for_remove_doctor)

doctor_manager.DisplayAll()