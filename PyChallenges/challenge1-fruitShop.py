# The fruits we want to sell: Apples, Bananas, Oranges and Pears.

# Fruit Prices:
  # Apple: £1
  # Banana: £1.15
  # Orange: £1.25
  # Pear: £1.85

apple = 1
banana = 1.15
orange = 1.25
pear = 1.85

global totalCost
totalCost = 0

global current
current = totalCost

global appleBought
appleBought = False

global bananaBought
bananaBought = False

global orangeBought
orangeBought = False

global pearBought
pearBought = False


def refund():
    global current
    current = totalCost

    global appleBought
    appleBought = False

    global bananaBought
    bananaBought = False

    global orangeBought
    orangeBought = False

    global pearBought
    pearBought = False

    if refundPrompt == "apple" and appleBought == True:
        appleBought = True
        print(f"Refunded apple! The total is: {current - 1}.")
    elif refundPrompt == "apple" and appleBought is not True:
        appleBought = False
        print("We cannot refund this item since you haven't bought it. \n")

    elif refundPrompt == "banana" and bananaBought == True:
        bananaBought = True
        print(f"Refunded banana! The total is: {current - 1.15}.")
    elif refundPrompt == "banana" and bananaBought is not True:
        bananaBought = False
        print("We cannot refund this item since you haven't bought it.\n")

    elif refundPrompt == "orange" and orangeBought == True:
        orangeBought = True
        print(f"Refunded orange! The total is: {current - 1.25}.")
    elif refundPrompt == "orange" and orangeBought is not True:
        orangeBought = False
        print("We cannot refund this item since you haven't bought it. \n")
        
    elif refundPrompt == "pear" and pearBought == True:
        pearBought = True
        print(f"Refunded pear! The total is: {current - 1.85}.")
    elif refundPrompt == "pear" and pearBought is not True:
        pearBought = False
        print("We cannot refund this item since you haven't bought it. \n")


def buy():
    global current
    current = totalCost

    global appleBought
    appleBought = False

    global bananaBought
    bananaBought = False

    global orangeBought
    orangeBought = False

    global pearBought
    pearBought = False

    if input_field == "apple":
        appleBought = True
        if appleBought == True:
            current = totalCost + 1
            print(f"Bought an apple successfully! Your current total is at £{current}.\n")
    elif input_field == "banana":
        bananaBought = True
        if bananaBought == True:
            current = totalCost + 1.15
            print(f"Bought a banana successfully! Your current total is at £{current}.\n")
    elif input_field == "orange":
        orangeBought = True
        if orangeBought == True:
            current = totalCost + 1.25
            print(f"Bought an orange successfully! Your current total is at £{current}.\n")
    elif input_field == "pear":
        pearBought = True
        if pearBought == True:
            current = totalCost + 1.85
            print(f"Bought a pear successfully! Your current total is at £{current}.\n")


while True:
    print("-- WELCOME! An apple costs £1, A banana is £1.15, An oranges costs £1.25 and a pear is £1.85. --")
    input_field = input("What'd you like to buy? ['FINISH' - ends session | 'REFUND' - get a refund (DOESN'T WORK PROPERLY)] ").lower()
    if input_field == "apple" or input_field == "banana" or input_field == "orange" or input_field == "pear":
        buy() 
    elif input_field == "nothing" or input_field == "":
        print(f"You bought nothing, your current total is: £{current}. \n")
    elif input_field == "finish":
        print(f"\n Thank you for shopping with us! The final total adds up to: £{current}.")
        print("We hope to see you again soon! \n")
        quit(0)
    elif input_field == "refund":
        # refundPrompt = print("\n Function does not work as intended. ").lower()
        # if refundPrompt == "apple" or refundPrompt == "banana" or refundPrompt == "orange" or refundPrompt == "pear":
            print("Function does not work as intended. \n")
            pass
         # else:
           # print("Function does not work as intended. \n")
           # pass
    else:
        print(f"\n Invalid input. The total is at £{current}. \n")