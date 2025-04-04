def list_operations():
    my_list=[]
    while True:
        print("\nList Operations:")
        print("1.Insert an element")
        print("2.Delete an element")
        print("3.Find an element")
        print("4.Display List")
        print("5.Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            ele=input("Enter element to insert: ")
            my_list.append(ele)
            print(f"Element '{ele}' inserted.")
        elif choice==2:
            ele=input("Enter element to delete: ")
            if ele in my_list:
                my_list.remove(ele)
                print(f"Element '{ele}' deleted.")
            else:
                print(f"Element '{ele}' not found.")
        elif choice==3:
            ele=input("Enter element to find: ")
            if ele in my_list:
                print(f"Element '{ele}' found.")
            else:
                print(f"Element '{ele}' not found.")
        elif choice==4:
            print(f"Current list:{my_list}")
        elif choice==5:
            break
        else:
            print("Invalid choice!!!!")
list_operations()