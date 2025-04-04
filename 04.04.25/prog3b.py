def merge_dictionaries():
    dict1 = {}
    dict2 = {}

    # Input first dictionary
    n1 = int(input("Enter number of elements for first dictionary: "))
    for _ in range(n1):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict1[key] = value

    # Input second dictionary
    n2 = int(input("Enter number of elements for second dictionary: "))
    for _ in range(n2):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict2[key] = value

    # Merging dictionaries
    merged_dict = dict1.copy()
    merged_dict.update(dict2)

    print("\nMerged Dictionary:", merged_dict)

# Run the function
merge_dictionaries()
