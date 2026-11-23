def Run():
    card_number = int(input("Enter your card number: "))
    remnant = card_number % 10
    match remnant:
        case 0 | 1:
            print("Відділення загальна терапія")
        case 2 | 3:
            print("Відділення хірургії")
        case 4 | 5:
            print("Відділення кардіології")
        case 6 | 7:
            print("Відділення неврології")
        case 8 | 9:
            print("Відділення офтальмології")
        case _:
            print("Невідоме відділення")

    concession_card = "так" if card_number % 2 == 0 else "Ні"
    review = "так" if card_number % 3 == 0 else "ні"

    print("Пільгова картка:", concession_card)
    print("Огляд:", review)