N = input("Choose A Number: ")

if N > 0:
    print(f"The number inputed ({N}) is positive.")
elif N < 0:
    print(f"The number inputed ({N}) is negative.")
else:
    print("Invalid input. Program shutting down.")
    quit()