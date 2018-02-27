sam = []
sammy = int(input('How many numbers: '))
for n in range(sammy):
    numbers = int(input('Enter number '))
    sam.append(numbers)
print("Minimum element in the list is :", min(sam))