def calc_interest(amount, rate, years):
    for n in range(years):
        amount = amount + (amount * rate)
    return amount

print(calc_interest(100.0, .10, 2))
