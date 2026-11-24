days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
counts = []
for i in range(len(days)):
    count = int(input(f"Enter quantity of the item for {days[i]}: "))
    counts.append(count)

print (f"List of item quantities for each day: {counts}")

total_count = 0
for i in range(len(days)):
    total_count += counts[i]

print(f"Total quantity of items for the week: {total_count}")

min_idx = counts[0]
max_idx = counts[0]
for c in counts:
    if c < min_idx:
        min_idx = c
    if c > max_idx:
        max_idx = c

print(f"Minimum quantity of items in a day: {days[counts.index(min_idx)]}: {min_idx}")
print(f"Maximum quantity of items in a day: {days[counts.index(max_idx)]}: {max_idx}")