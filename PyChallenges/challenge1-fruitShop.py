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


def refund():
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
    elif refundPrompt == "apple" and appleBought == False:
        appleBought = False
        print("We cannot refund this item since you haven't bought it. \n")

    elif refundPrompt == "banana" and bananaBought == True:
        bananaBought = True
        print(f"Refunded banana! The total is: {current - 1.15}.")
    elif refundPrompt == "banana" and bananaBought == False:
        bananaBought = False
        print("We cannot refund this item since you haven't bought it.\n")

    elif refundPrompt == "orange" and orangeBought == True:
        orangeBought = True
        print(f"Refunded orange! The total is: {current - 1.25}.")
    elif refundPrompt == "orange" and orangeBought == False:
        orangeBought = False
        print("We cannot refund this item since you haven't bought it. \n")
        
    elif refundPrompt == "pear" and pearBought == True:
        pearBought = True
        print(f"Refunded pear! The total is: {current - 1.85}.")
    elif refundPrompt == "pear" and pearBought == False:
        pearBought = False
        print("We cannot refund this item since you haven't bought it. \n")


def buy():
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
    input_field = input("What'd you like to buy? ['FINISH' will end the session | 'REFUND' to get a refund.] ").lower()
    if input_field == "apple" or input_field == "banana" or input_field == "orange" or input_field == "pear":
        buy() 
    elif input_field == "nothing" or input_field == "":
        print(f"You bought nothing, your current total is: £{current}. \n")
    elif input_field == "finish":
        print(f"\n Thank you for shopping with us! The final total adds up to: £{current}.\n")
        quit(0)
    elif input_field == "refund":
        refundPrompt = input("\n Which item would you like to refund? ").lower()
        if refundPrompt == "apple" or refundPrompt == "banana" or refundPrompt == "orange" or refundPrompt == "pear":
            refund()
        else:
            print("No item to refund. \n")
    else:
        print(f"\n Invalid input. The total is at £{current}. \n")