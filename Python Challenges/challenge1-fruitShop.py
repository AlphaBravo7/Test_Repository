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

totalCost = 0


def buy():
    if input_field == "apple":
        appleBought = True
        if appleBought == True:
            totalCost = totalCost + 1
            print(f"Bought an apple successfully! Your current total is at £{totalCost}.")
    elif input_field == "banana":
        bananaBought = True
        if bananaBought == True:
            totalCost = totalCost + 1.15
            print(f"Bought a banana successfully! Your current total is at £{totalCost}.")
    elif input_field == "orange":
        orangeBought = True
        if orangeBought == True:
            totalCost = totalCost + 1.25
            print(f"Bought an orange successfully! Your current total is at £{totalCost}.")
    elif input_field == "pear":
        pearBought = True
        if pearBought == True:
            totalCost = totalCost + 1.85
            print(f"Bought a pear successfully! Your current total is at £{totalCost}.")


print("-- WELCOME! This is a fruit shop. Apples cost £1 each, Bananas are £1.15 each, Oranges cost £1.25 each and Pears are £1.85 each.  --")
input_field = input("What'd you like to buy? ['FINISH' will end the session.] ").lower()
if input_field != "nothing" or input_field != "":
    buy() 
elif input_field == "nothing" or input_field == "":
    print(f"You bought nothing, your current total is: £{totalCost}.")
elif input_field == "finish":
    print(f"Thank you for shopping with us! The final total adds up to: £{totalCost}.")
else:
    print(f"Invalid input. The total is at £{totalCost}.")
    quit()