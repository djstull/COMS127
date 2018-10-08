def process_date(date):
#US Date Format: IE: 10/01/18 converted to October 1, 2018
    day = int(date[3:5])
    month = int(date[:2])
    year = date[6:]
    months = ["January","February","March","April","May","June","July", \
              "Augest","September","October","November","December"]
    return months[month - 1] + " " + str(day) + ", 20" + year

print(process_date("03/01/00"))