name = input("Hello, what is your name? ")
gender = input(f"Ok {name}, what is your gender? (M/F) ").lower()

def check():
    if gender == "m":
        print(f"Hello, Mr. {name}.")
    elif gender == "f":
        print(f"Hello, Mrs. {name}.")
    else:
        if gender != "m" or "f":
            print("Invalid input.")
            quit()

check()