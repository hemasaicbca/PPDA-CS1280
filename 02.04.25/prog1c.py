def find_largest():
    print("Find the largest of three numbers")
    n1=float(input("Enter first number : "))
    n2=float(input("Enter second number : "))
    n3=float(input("Enter third number : "))
    if n1>=n2 and n1>=n3:
        largest=n1
    elif n2>=n1 and n2>=n3:
        largest=n2
    else:
        largest=n3
    print(f"The largest number is : {largest}")
find_largest()