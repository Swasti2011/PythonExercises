num=int(input("Enter a number: "))
for i in range (2,num):
    if num%i==0:
        print("The number you entered is NOT a PRIME number.")
        break
else:
    print("The number you entered is a PRIME number.")