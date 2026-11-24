class Task8:
    def CalculateBMI(weight, height):
        return weight / (height ** 2) * 10000

    def GetBMICategory(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def CalculateCost(price, count, discount):
        return price * count * (1 - discount / 100.0)

    def GetAgeCategory(age):
        if age < 13:
            return "Child"
        elif 13 <= age < 20:
            return "Teenager"
        elif 20 <= age < 65:
            return "Adult"
        else:
            return "Senior"

    def GetPressureStatus(systolic, diastolic):
        if systolic < 120 and diastolic < 80:
            return "Normal"
        elif 120 <= systolic < 130 and diastolic < 80:
            return "Elevated"
        elif (130 <= systolic < 140) or (80 <= diastolic < 90):
            return "High Blood Pressure (Hypertension) Stage 1"
        elif (140 <= systolic) or (90 <= diastolic):
            return "High Blood Pressure (Hypertension) Stage 2"
        else:
            return "Hypertensive Crisis"

    def Run():
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi = Task8.CalculateBMI(weight, height)
        print(f"BMI: {bmi:.2f}, Category: {Task8.GetBMICategory(bmi)}")

        price = float(input("Enter price of the item: "))
        count = int(input("Enter quantity of the item: "))
        discount = float(input("Enter discount percentage: "))
        total_cost = Task8.CalculateCost(price, count, discount)
        print(f"Total cost after discount: ${total_cost:.2f}")

        age = int(input("Enter age: "))
        print(f"Age category: {Task8.GetAgeCategory(age)}")

        systolic = int(input("Enter systolic blood pressure: "))
        diastolic = int(input("Enter diastolic blood pressure: "))
        print(f"Blood pressure status: {Task8.GetPressureStatus(systolic, diastolic)}")

Task8.Run()