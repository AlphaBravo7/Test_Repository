number = int(input("Pleace input a number: "))
sqr_cube = input("Should the number be squared or cubed? ").lower()

if sqr_cube == "squared":
    def Square_number():
        Sqrd_number = number * number
        print(f"'{number}' squared is equal to '{Sqrd_number}'!")
    Square_number()
    quit()

elif sqr_cube == "cubed":
    def Cubed_num():
        Cubed_number = number * number
        print(f"'{number}' squared is equal to '{Cubed_number}'!")
    Cubed_num()
    quit()