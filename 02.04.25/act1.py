def calculator():
    print("Simple Calculator")
    n1=float(input("Enter first number:"))
    n2=float(input("Enter second number:"))
    print("Select operation:")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Exponentiation")
    print("7.Floor Division")
    choice=input("Enter choice(1/2):")
    if choice=='1':
        print(f"Result:{n1}+{n2}={n1+n2}")
    elif choice=='2':
        print(f"Result:{n1}-{n2}={n1-n2}")
    elif choice=='3':
        print(f"Result:{n1}*{n2}={n1*n2}")
    elif choice=='4':
        if n2!=0:
         print(f"Result:{n1}/{n2}={n1/n2}")
        else:
           print("Error! Division by zero.")
    elif choice=='5':
        if n2!=0:
         print(f"Result:{n1}%{n2}={n1%n2}")
        else:
           print("Error! Division by zero.")
    elif choice=='6':
        print(f"Result:{n1}^{n2}={n1**n2}")
    elif choice=='7':
        if n2!=0:
         print(f"Result:{n1}//{n2}={n1//n2}")
        else:
           print("Error! Division by zero.")
    
    else:
       print("Invalid option")
calculator()