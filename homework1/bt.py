# David James (DJ) Stull
# Com S 127


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
    if n < 0:
        isneg = True
    elif n > 0:
        isneg = False
    else:
        isneg = "Zero"

    if isneg is True:
        n = str(n)
        n = n.replace("-", "")
    else:
        pass

    n = str(n)
    counter = len(n)
    print(counter)
    n = int(n)

    output = ""

    while counter >= 0:
        conv = (n % 3)
        if conv == 0:
            output = output + "0"
        elif conv == 1:
            output = output + "+"
        elif conv == -1:
            output = output + "-"
        counter = counter - 1
    return output




def negate(n):
    # Makes any balanced ternary number negative.
    # It replaces + with NULL first in order to avoid copying over the newly replaced - characters.

    for i in n:
        n = n.replace("+", "NULL")
        n = n.replace("-", "+")
        n = n.replace("NULL", "-")
    return n


def is_valid_balanced_ternary(n):
    # Checks to see if "+", "-", or "0" are the only characters in a number,
    # if they are, returns TRUE because it is balanced ternary number.

    # Checks to see if n is an int, and converts it to a string.
    isint = isinstance(n, int)
    if isint is True:
        n = str(n)

    return set(n).issubset({"+", "-", "0"})

# Test cases for BALANCED TERNARY CHECK -- Complete
# print(is_valid_balanced_ternary("+-+--0-+0"))
# print(is_valid_balanced_ternary("---------"))
# print(is_valid_balanced_ternary("+++++++r++"))
# print(is_valid_balanced_ternary("000000000"))

# Test cases for NEGATE -- Complete
# print(negate("+-+--0-+0"))
# print(negate("+++++++++"))
# print(negate("---------"))
# print(negate("000000000"))

# Test cases for CONVERT TO DECIMAL -- Complete
# print(convert_to_decimal("+-+--0-+0"))
# ^ Should be 4773
# print(convert_to_decimal("-+++0-"))
# ^ Should be -127
# print(convert_to_decimal("++"))
# ^ Should be 4
# print(convert_to_decimal(69))
# ^ Should print error and return 0


# Test cases for CONVERT TO BALANCED TERNARY -- Incomplete
print(convert_to_balanced_ternary(4))
# ^ Should return ++
print(convert_to_balanced_ternary(4773))
# ^ Should return +-+--0-+0
