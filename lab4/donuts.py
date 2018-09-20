def donut_break(numd):
    amount = numd
    dozens = amount // 12
    amount = amount - (dozens * 12)

    cost = amount * .75
    cost = cost + (dozens * 8)

    print ("$", cost)