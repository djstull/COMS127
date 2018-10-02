def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (n-1)

print(factorial(3))

def cal_interest(amount, rate, years):
    total = (amount * rate)
    