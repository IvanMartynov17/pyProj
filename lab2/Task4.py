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

#рядок = лікар, стовпець = робочий день. Значення — кількість прийомів

#5 3 4 2 8 1 6 2 7
for i in range(rows):
    print(f"Doctor {i + 1} appointments for the week: {sum(matrix[i])} appointments")

for j in range(cols):
    print (f"Days: {j + 1} appointments for the week: {sum(matrix[i][j] for i in range(rows))} appointments")

max = matrix[0][0]
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > max:
            max = matrix[i][j]

print(f"Maximum number of appointments in a day: {max} appointments")