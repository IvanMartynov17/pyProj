count = int(input("Enter quantity of the item: "))
price = []
for i in range(count):
    p = int(input(f"Enter price for item {i + 1}: "))
    price.append(p)

print (f"List of item prices: {price}")

sorted_prices = sorted(price)
sorted_prices_desc = sorted(price, reverse=True)


min = price[0]
max = price[0]

for p in price:
    if p < min:
        min = p
    if p > max:
        max = p

print(f"Minimum price: {min}")
print(f"Maximum price: {max}")
print (f"Sorted list of item prices in descending order: {sorted_prices_desc}")
print (f"Sorted list of item prices: {sorted_prices}")