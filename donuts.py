#Get initial amount of donuts
amount = int(input("Hello sir! How many donuts would you like?: "))

#Determine the amount of dozens an subtract that many donuts from the total
dozens = amount // 12
amount = amount - (dozens * 12)

cost = amount * .75
cost = cost + (dozens * 8)

print ("$", cost)
print (dozens, "Dozen")
print (amount, "Singles")