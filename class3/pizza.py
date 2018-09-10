toppings = int(input("How many toppings would you like?: "))
pizza = 12
cost = pizza + (toppings * .75)
if cost > 16:
    cost = 16
print("Your total is: $" + cost)
