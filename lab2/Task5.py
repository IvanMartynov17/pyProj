matrix = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter value for element [{i + 1}][{j + 1}]: "))
        row.append(value)
    matrix.append(row)

for row in matrix:
    for value in row:
        print(value, end="\t")
    print()

sum = 0
for i in range(rows):
    for j in range(cols):
        if i == j:
            print (f"Element [{i + 1}][{j + 1}] = {matrix[i][j]}")
            sum += matrix[i][j]

print(f"Sum of diagonal elements: {sum}")

sum2 = 0

for i in range(rows):
    for j in range(cols):
        if i + j == rows - 1:
            print (f"Element [{i + 1}][{j + 1}] = {matrix[i][j]}")
            sum2 += matrix[i][j]

print(f"Sum of anti-diagonal elements: {sum2}")