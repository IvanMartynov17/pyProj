def Run():
    price = float(input("Enter the price: "))
    count = int(input("Enter the count: "))
    discount = int(input("Enter the discount: "))

    sum = price * count * (1 - discount / 100)
    print(f"The sum is = {sum:.2f}")