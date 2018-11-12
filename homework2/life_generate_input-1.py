import random
import math

x = int(input())
y = int(input())
print(x)
print(y)
print(-1)
i = 0
while (i < math.ceil(x * y * .25)):
    print(random.randint(0, x - 1), random.randint(0, y - 1))
    i += 1
