def main():
    import random
    print("This an RNG (Random Number Generator)")

    totalNumGnrtd = 0

    while True:
        yn = input("Generate a random number between 1 and 100? (Y/N) ").lower()
        if yn == "y":
            randomN = random.randint(1, 100)
            totalNumGnrtd += 1
            print(f"Your random number generated is: {randomN}. \n")
            while True:    
                totalChecker = input("Would you like to see the total of numbers generated in this session? (Y/N) ").lower()
                if totalChecker == "y":
                    print(f"The total amount of numbers generated in this session is: {totalNumGnrtd}. \n")
                if totalChecker == "n":
                    break
        if yn == "n":
            print("Program quit.")
            quit(0)

main()