from lab3.patient import Patient

p1 = Patient("Martynov", "Ivan", "02.12.2008", "A+", "+380999999999",
             "ivan.martynov@gmail.com", 17)
p2 = Patient("Smith", "John", "01.01.1990", "O-", "+1234567890",
             "john.smith@example.com", 31)
p3 = Patient("Doe", "Jane", "15.05.1985", "B+", "+9876543210",
             "jane.doe@example.com", 36)
p1.show()
p1.GetAgeCategory()
print("\n")

p2.show()
p2.GetAgeCategory()
print("\n")

p3.show()
p3.GetAgeCategory()
print("\n")

#first_name, last_name, date_of_birth, blood_type, phone, email, full_name, age, is_adult