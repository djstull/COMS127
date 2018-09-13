num = int(input("How many burritos would you like?: "))
zipcode = int(input("What zip code are you located in?: "))
cost = num * 6

if num >= 6:
    if zipcode == 50011:
        delivery = 0
    else:
        delivery = 5
else:
    if zipcode == 50011:
        delivery = 3
    else:
        delivery = 5

total = cost + delivery
print("Your total comes to: $" + str(total))