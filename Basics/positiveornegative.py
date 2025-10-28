ch="y"
while ch=="y":
    num=int(input("Enter a number: "))
    if num>0:
        print(f"{num} is positive.")
    elif num<0:
        print(f"{num} is Negative.")
    else:
        print(f"{num} is Zero.")
    ch=input("Do you want to continue (y/n): ")