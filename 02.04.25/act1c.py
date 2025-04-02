def find_largest():
    print("Find the largest of five numbers")
    n1=float(input("Enter first number : "))
    n2=float(input("Enter second number : "))
    n3=float(input("Enter third number : "))
    n4=float(input("Enter fourth number : "))
    n5=float(input("Enter fifth number : "))
    if n1>=n2 and n1>=n3 and n1>=n4 and n1>=n5:
        largest=n1
    elif n2>=n1 and n2>=n3 and n2>=n4 and n2>=n5:
        largest=n2
    elif n3>=n1 and n3>=n2 and n3>=n4 and n3>=n5:
        largest=n3
    elif n4>=n1 and n4>=n2 and n4>=n3 and n4>=n5:
        largest=n4
    else:
        largest=n5
    print(f"The largest number is : {largest}")
find_largest()