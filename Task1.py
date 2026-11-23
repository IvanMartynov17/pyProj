def Run():
    weight = float(input("Enter your weight:"))
    height = float(input("Enter your height:"))
    imt = weight / (height * height)
    imt *= 1000
    print(f"Your IMT is: {imt:.2f}")
