burritos = int(input("How many burritos would you like?: "))
zipcode = int(input("Please input the zip code for delivery: "))
if zipcode == 50011:
    cost = (burritos * 6)
else:
    cost = (burritos * 6) + 5
print("Your total is $" + str(cost))