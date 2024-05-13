# The fruits we want to sell: Apples, Bananas, Oranges and Pears.

# Fruit Prices:
  # Apple: £1
  # Banana: £1.15
  # Orange: £1.25
  # Pear: £1.85

appleBought = False
bananaBought = False
orangeBought = False
pearBought = False

apple = 1
banana = 1.15
orange = 1.25
pear = 1.85

global totalCost
totalCost = 0

global current
current = totalCost


def buy():
    if input_field == "apple":
        appleBought = True
        if appleBought == True:
            current = totalCost + 1
            print(f"Bought an apple successfully! Your current total is at £{current}.")
    elif input_field == "banana":
        bananaBought = True
        if bananaBought == True:
            current = totalCost + 1.15
            print(f"Bought a banana successfully! Your current total is at £{current}.")
    elif input_field == "orange":
        orangeBought = True
        if orangeBought == True:
            current = totalCost + 1.25
            print(f"Bought an orange successfully! Your current total is at £{current}.")
    elif input_field == "pear":
        pearBought = True
        if pearBought == True:
            current = totalCost + 1.85
            print(f"Bought a pear successfully! Your current total is at £{current}.")

while True:
    print("-- WELCOME! An apple costs £1, A banana is £1.15, An oranges costs £1.25 and a pear is £1.85. --")
    input_field = input("What'd you like to buy? ['FINISH' will end the session.] ").lower()
    if input_field == "apple" or input_field == "banana" or input_field == "orange" or input_field == "pear":
        buy() 
    elif input_field == "nothing" or input_field == "":
        print(f"You bought nothing, your current total is: £{current}.")
    elif input_field == "finish":
        print(f"Thank you for shopping with us! The final total adds up to: £{current}.")
    else:
        print(f"Invalid input. The total is at £{current}.")
        break