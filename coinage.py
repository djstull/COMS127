#Write a program to calculate the coinage needed for a given amount of change.
amount = int(input('Please input the amount of cents: '))

quarters = amount // 25
amount = amount % 25
dimes = amount // 10
amount = amount % 10
nickels = amount // 5
pennies = amount % 5

print(' ')
print(quarters, "quarters\n")
print(dimes, "dimes\n")
print(nickels, "nickels\n")
print(pennies, "pennies\n")