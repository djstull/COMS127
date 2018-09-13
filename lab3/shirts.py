shirt = int(input("How many shirts would you like?: "))
state = input("Do you live in Minnesota? (y,n): ")

cost = shirt * 10

if shirt < 30:
        cost = cost + 50

if state in ['y']:
    cost = cost * 1.05

print(cost)