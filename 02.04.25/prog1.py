def calculator():
    print("Simple Calculator")
    n1=float(input("Enter first number:"))
    n2=float(input("Enter second number:"))
    print("Select operation:")
    print("1.Add")
    print("2.Divide")
    choice=input("Enter choice(1/2):")
    if choice=='1':
        print(f"Result:{n1}+{n2}={n1+n2}")
    elif choice=='2':
        if n2!=0:
         print(f"Result:{n1}/{n2}={n1/n2}")
        else:
           print("Error! Division by zero.")
    else:
       print("Invalid option")
calculator()