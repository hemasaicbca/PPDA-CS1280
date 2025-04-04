
dict1 = {}
n1 = int(input("Enter number of elements for first dictionary: "))
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    
    dict1[key] = int(value) if value.isdigit() else value


dict2 = {}
n2 = int(input("Enter number of elements for second dictionary: "))
for _ in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    
    dict2[key] = int(value) if value.isdigit() else value

merged_dict = dict1.copy() 

for key, value in dict2.items():
    if key in merged_dict:

        if isinstance(merged_dict[key], int) and isinstance(value, int):
            merged_dict[key] += value
        else:
           
            merged_dict[key] = str(merged_dict[key]) + str(value)
    else:
        merged_dict[key] = value


print("\nMerged Dictionary:", merged_dict)
