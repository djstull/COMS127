# David James (DJ) Stull
# Com Sci 127
# This script has four functions that are all useful in converting back and forth in between decimal (base 10) numbers
# and balanced ternary numbers.

def convert_to_decimal(n):
    # Takes any balanced ternary number and converts it to the base 10 decimal equivalent.

    balanced = is_valid_balanced_ternary(n)
    if balanced is True:
        places = len(n) - 1
        counter = places
        result = 0

        for i in n:
            if i == "-":
                term = -1
            elif i == "+":
                term = 1
            else:
                term = 0

            result = result + (term * (pow(3, counter)))
            counter = counter - 1
        return result

    elif balanced is False:
        print("ERROR: n is not a balanced ternary.")
        return 0


def convert_to_balanced_ternary(n):
    # Converts a decimal number to a balanced ternary number.

    if n == 0:
        return ['0']

    # Check for negative numbers
    neg = (n < 0)
    if neg:
        n *= -1

    rem = 0
    out = []

    while n >= 0 and not (n == 0 and rem == 1):
        rem, n = n % 3, n // 3
        if rem == 0:
            out.append('0')
        elif rem == 1:
            out.append('+')
        else:
            out.append('-')
            n += 1
    out.reverse()

    # Finally outputs the balanced ternary form of the decimal number. If the decimal was negative,
    # outputs the negate of the outputted balanced ternary instead.

    if neg:
        out = "".join(out)
        outneg = negate(out)
        return outneg
    else:
        out = "".join(out)
        return out


def negate(n):
    # Makes any balanced ternary number negative.
    # Builds the negated string character by character.

    balanced = is_valid_balanced_ternary(n)
    neg = ""
    if balanced is True:
        for i in n:
            if i == "+":
                neg = neg + "-"
            elif i == "-":
                neg = neg + "+"
            elif i == "0":
                neg = neg + "0"
            else:
                pass
        return neg
    else:
        print("ERROR: n is not a balanced ternary.")
        return 0


def is_valid_balanced_ternary(n):
    # Checks to see if "+", "-", or "0" are the only characters in a number,
    # if they are, returns TRUE because it is balanced ternary number.

    # Checks to see if n is an int, and converts it to a string.
    isint = isinstance(n, int)
    if isint is True:
        n = str(n)

    return set(n).issubset({"+", "-", "0"})

# See bt_test.py for numerous test cases for each of the functions/
