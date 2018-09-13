hours = int(input("How long did your work this pay period? (hrs): "))
status = input("Are you exempt from overtime hours? (y,n): ")
hourly_rate = int(input("How much do you get paid and hour?: "))

if status in ['y']:
    wage = hours * hourly_rate
else:
    wage
    if hours > 40:
        overtime = hours - 40
        wage = (hours * hourly_rate) + (overtime * (hourly_rate * 5.5))
    else:
        wage = hours * hourly_rate
print(wage)