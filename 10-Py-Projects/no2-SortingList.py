def Sort():
    List = [6, 1, 2, 9, 3, 4, 8, 5, 7, 10]
    print(f"{List} is a list of numbers.\n")
    params = ["asc", "desc", "none"]
    ask = input("Do you want to display the list in ascending order (asc), descending order (desc), or keep it the same (none)? ").lower()
    if ask == params[0]:
        List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(List)
    elif ask == params[1]:
        List = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        print(List)
    elif ask == params[2]:
        List = [6, 1, 2, 9, 3, 4, 8, 5, 7, 10]
        print(List)
    else:
        print("Invalid input, program will shut down.\n")
        quit()

Sort()