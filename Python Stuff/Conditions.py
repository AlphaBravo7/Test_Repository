N = input("Choose A Number: ")
N = int(N)
try:
    if N > 0:
        print(f"The number inputed ({N}) is positive.")
    elif N < 0:
        print(f"The number inputed ({N}) is negative.")
    elif N == 0:
        print("The number equals 0.")
except:
    print("Invalid input. Program shutting down.")
    quit()