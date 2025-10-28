a=int(input("Enter first number: "))
operator=input("Enter operator (+, -, *, /): ")
b=int(input("Enter second number: "))
if operator=='+':
    print(f"{a} + {b} = {a+b}")
elif operator=='-':
    print(f"{a} - {b} = {a-b}")
elif operator=='*':
    print(f"{a} * {b} = {a*b}")
elif operator=='/':
    print(f"{a} / {b} = {a/b}")
else:
    print("Invalid operator")
    