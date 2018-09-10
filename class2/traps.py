print("Welcome to bettertraps.info! Your only source for the best traps in the land.")
print("Order more than 30 traps today, and get free shipping!")
num_mousetraps = int(input("Yo, how many traps you want?: "))
if num_mousetraps < 30:
    shipping = .5 * num_mousetraps
else:
    shipping = 0
total_cost = (num_mousetraps * 5) + shipping
print("Yo, your traps are gonna come to: $" + str(total_cost))