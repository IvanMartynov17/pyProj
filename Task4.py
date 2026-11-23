def Run():

    systolic_pressure = int(input("Enter your systolic pressure: "))
    diastolic_pressure = int(input("Enter your diastolic pressure: "))

    if systolic_pressure < 120 and diastolic_pressure < 80:
        print("Your blood pressure is normal.")
    else:
        if systolic_pressure < 130 and diastolic_pressure < 80:
            print("Your blood pressure is high.")
        else:
            if systolic_pressure < 140 or diastolic_pressure < 90:
                print("Hypertonia 1st stage.")
            else:
                print("Hypertonia 2nd stage.")