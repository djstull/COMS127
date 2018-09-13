#This is my second attempt at wages. Hopefully it goes better this time.

#hours is the total amount of hours they worked in the given span.
hours = int(input("How many hours did you work?: "))
#hourly displays how much money the person makes per hour.
hourly = int(input("How much money do you make per hour?: "))
#status = displays y (yes) if they are exempt or n (no) if they are non-exempt for overtime pay.
status = str(input("Are you exempt from overtime pay? (y or n): "))

if status in ["y"]:
    wage = hours * hourly
elif status in ["n"]:
    #overtime determines how many hours over 40 the person has worked.
    overtime = (hours - 40)
    hours = (hours - overtime)
    wage = (hours * hourly) + ( overtime * 5.5)
else:
    pass

#prints the total amount of money earned
print("Total Earnings: $" + str(wage))
