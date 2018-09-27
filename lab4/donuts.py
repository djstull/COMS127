#numd stands for the number of donuts - the rest of the function is adapted from my old donuts.py
def donut_break(numd):
    amount = numd
    dozens = amount // 12
    amount = amount - (dozens * 12)

    cost = amount * .75
    cost = cost + (dozens * 8)

    print ("$", cost)