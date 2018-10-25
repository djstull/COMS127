# David James (DJ) Stull
# Com Sci 127
# This script has a number of test cases for the functions that are declared in bt.py.
from bt import negate, is_valid_balanced_ternary, convert_to_balanced_ternary, convert_to_decimal
#
# Helper functions for testing
# ============================
#


def test_convert_to_decimal(arg, expected):
    '''
    Checks result for is_valid_digit_group
    '''
    actual = convert_to_decimal(arg)
    if expected != actual:
        print("ERROR: convert_to_decimal(" + str(arg) + ")")
        print("Expected:", expected, "Actual:", actual)

    
def test_convert_to_balanced_ternary(arg, expected):
    '''
    Checks result for convert_to_balanced_ternary
    '''
    actual = convert_to_balanced_ternary(arg)
    if expected != actual:
        print("ERROR: convert_to_balanced_ternary(" + str(arg) + ")")
        print("Expected:", expected, "Actual:", actual)


def test_negate(arg, expected):
    '''
    Checks result for negate
    '''
    actual = negate(arg)
    if expected != actual:
        print("ERROR: negate(" + str(arg) + ")")
        print("Expected:", expected, "Actual:", actual)


def test_is_valid_balanced_ternary(arg, expected):
    '''
    Checks result for is_valid_balanced_ternary
    '''
    actual = is_valid_balanced_ternary(arg)
    if expected != actual:
        print("ERROR: is_valid_balanced_ternary(" + str(arg) + ")")
        print("Expected:", expected, "Actual:", actual)


# Test cases for negate()
# 0 should be 0
test_negate("0", "0")

# + should be -
test_negate("+", "-")

# - should be +
test_negate("-", "+")

# -------- should be ++++++++
test_negate("--------", "++++++++")

# +0- should be -0+
test_negate("+0-", "-0+")

# +-00-0-0-00-+ should be -+00+0+0+00+-
test_negate("+-00-0-0-00-+", "-+00+0+0+00+-")

# 2 is not valid -- Should output an ERROR stating that it is not a balanced ternary.
test_negate("2", "0")

# --+00+a0- is not valid -- Should output an ERROR stating that it is not a balanced ternary.
test_negate("--+00+a0-", "0")

# Test cases for BALANCED TERNARY CHECK -- Complete
test_is_valid_balanced_ternary("+-+--0-+0", True)
test_is_valid_balanced_ternary("---------", True)
test_is_valid_balanced_ternary("+++++++r++", False)
test_is_valid_balanced_ternary("000000000", True)

# Test cases for NEGATE -- Complete
test_negate("+-+--0-+0", "-+-++0+-0")
test_negate("+++++++++", "---------")
test_negate("---------", "+++++++++")
test_negate("000000000", "000000000")

# Test cases for CONVERT TO DECIMAL -- Complete
test_convert_to_decimal("+-+--0-+0", 4773)
# ^ Should be 4773
test_convert_to_decimal("-+-++0+-0", -4773)
# ^ Should be 4773
test_convert_to_decimal("-+++0-", -127)
# ^ Should be -127
test_convert_to_decimal("++", 4)
# ^ Should be 4
test_convert_to_decimal(69, 0)
# ^ Should print error and return 0


# Test cases for CONVERT TO BALANCED TERNARY -- Complete
test_convert_to_balanced_ternary(4, "++")
# ^ Should return ++
test_convert_to_balanced_ternary(4773, "+-+--0-+0")
# ^ Should return +-+--0-+0
test_convert_to_balanced_ternary(-4773, "-+-++0+-0")
# ^ Should return -+-++0+-0
