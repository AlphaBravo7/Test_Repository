import random, time

print("-- This is a test for more complicated code --")

def dealing_with_invalid_inputs():
    print("The input is invalid. Program will quit.")
    quit(0)

def main():
    global creatureHP
    creatureHP = 100

    global yourHP
    yourHP = 100

    prompt0 = input("Start? Y/N ").lower()
    if prompt0 == "y":
        prompt1 = input("We have found a creature, Do you wish to approach it or run? (Run/Approach) ").lower()
        if prompt1 == "run":
            print("You ran away from the creature.\n")
            quit()
        elif prompt1 == "approach":
            print("You approached the creature, it is now on the defensive. \n")
            while creatureHP > 0:
                prompt2 = input("Attack? (Y/N) ").lower()
                if prompt2 == "y":
                    randomNumber = random.randint(5, 21)
                    dmg_dealt = randomNumber
                    creatureHP -= dmg_dealt
                    print(f"You attacked the creature and dealt {dmg_dealt} damage! The creature's HP is at: {creatureHP}. Your current HP is: {yourHP}. \n")
                if yourHP > 0 and creatureHP < 0 or creatureHP == 0:
                    print("YOU WON!")
                    break
                elif prompt2 == "n":
                    randomNumber2 = random.randint(5, 21)
                    dmg_taken = randomNumber2
                    yourHP -= dmg_taken
                    print(f"The creature attacked you and dealt {dmg_taken} damage! The creature's HP is at: {creatureHP}. Your current HP is: {yourHP}. \n")
                if yourHP < 0 or yourHP == 0 and creatureHP > 0:
                    print("YOU LOSE!")
                    break
        else:
            dealing_with_invalid_inputs()
    elif prompt0 == "n":
        print("Proceed to continue the test.")
        quit(0)
    else:
        dealing_with_invalid_inputs()


main()