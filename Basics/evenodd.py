ch="y"
while ch=="y":
    num=int(input("Enter a number: "))
    if num%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    ch=input("Do you want to continue (y/n): ")