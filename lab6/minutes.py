def minutes(time):
    if len(time) == 4:
        hours = int(time[:1])
        minutes = int(time[2:])
        totalminutes = ((hours*60) + minutes)
        print(totalminutes)
    else:
        hours = int(time[:2])
        minutes = int(time[3:])
        totalminutes = ((hours*60) + minutes)
        print(totalminutes)

minutes("1:20")
minutes("10:20")
