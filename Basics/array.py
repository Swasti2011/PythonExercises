numbers = [1, 2, 3, 4, 5, 10, 15, 20]
a=int(input("Enter a number to search: "))
if a in numbers:
    print(f"{a} is found in the array")
else:
    print(f"{a} is not found in the array")
# This code checks if a user-input number is present in the predefined list 'numbers'.