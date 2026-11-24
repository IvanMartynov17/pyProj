count = int(input("Enter quantity of the patient weight: "))
weight = []
for i in range(count):
    w = float(input(f"Enter weight for patient {i + 1} in kg: "))
    weight.append(w)


min = weight[0]
max = weight[0]

for w in weight:
    if w < min:
        min = w
    if w > max:
        max = w

weight_more_than_avg = 0
for w in weight:
    if w > (sum(weight) / len(weight)):
        weight_more_than_avg += 1

print(f"List of patient weights: {weight}")
print ("\t==Звіт==")
print(f"Count of patients: {count}")
print(f"Average weight: {sum(weight) / len(weight):.2f} kg")
print(f"Minimum weight: {min:.2f} kg")
print(f"Maximum weight: {max:.2f} kg")
print (f"Count of patients with weight more than average: {weight_more_than_avg}")

 



