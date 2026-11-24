from itertools import count


def Run():
    count = int(input("Enter a count of numbers: "))
    numbers = []
    for i in range(count):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    average = sum(numbers) / len(numbers)
    
    min = numbers[0]
    max = numbers[0]
    
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
    num_more_than_average = 0
    
    for i in range(count):
        if (numbers[i] > average):
            num_more_than_average += 1
    number_more_than_thousand = 0
    
    for i in range(count):
        if (numbers[i] > 1000):
            number_more_than_thousand += 1
            
    print(f"List of numbers: {numbers}")
    print("==Звіт по прийомам==")
    print(f"Кількість: {len(numbers)}")
    print(f"Сума: {sum(numbers)}")
    print(f"Середнє: {average}")
    print(f"Мінімальне: {min}")
    print(f"Максимальне: {max}")
    print(f"Кількість чисел, що більші за середнє: {num_more_than_average}")
    print(f"Кількість чисел, що більші за 1000: {number_more_than_thousand}")

Run()