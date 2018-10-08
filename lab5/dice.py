#Rolls a dice - number is amount of dice - amount is the amount of times to roll the dice.
import random
count = 0
for n in range(1000):
    total = random.randrange(1, 7) + random.randrange(1, 7)
    if total == 7:
        count = count + 1
print(count)

