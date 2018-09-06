#Write a program to calculate the coinage needed for a given amount of change.
amount = int(input('Please input the total change in cents): '))

hundreds = amount // 10000
amount = amount % 10000
fifties = amount // 5000
amount = amount % 5000
twenties = amount // 2000
amount = amount % 2000
tens = amount // 1000
amount = amount % 1000
fives = amount // 500
amount = amount % 500
ones = amount // 100
amount = amount % 100
quarters = amount // 25
amount = amount % 25
dimes = amount // 10
amount = amount % 10
nickels = amount // 5
pennies = amount % 5

print(' ')
if hundreds > 0:
    print(hundreds, "hundreds\n")
if fifties > 0:
    print(fifties, "fifties\n")
if twenties > 0:
    print(twenties, "twenties\n")
if tens > 0:
    print(tens, "tens\n")
if fives > 0:
    print(fives, "fives\n")
if ones > 0:
    print(ones, "ones\n")
if quarters > 0:
    print(quarters, "quarters\n")
if dimes > 0:
    print(dimes, "dimes\n")
if nickels > 0:
    print(nickels, "nickels\n")
if pennies > 0:
    print(pennies, "pennies\n")