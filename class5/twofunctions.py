def max(num1, num2):
    if num1 > num2:
        largest = num1
    elif num2 > num1:
        largest = num2
    return largest

print(max(4, 5))
print(max(8, 9))
print(max(-4, -5))
print(max(4000, 6000))

def is_div(divend, divise):
    if divend % divise == 0:
        return True
    else:
        return False

#the if and else are redundant

print(is_div(4, 4))
print(is_div(3, 2))