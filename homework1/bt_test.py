from bt import is_balanced_ternary

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

#
# Test cases for negate()
# =====================================
#

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

# 2 is not valid
test_negate("2", "")

# --+00+a0- is not valid
test_negate("--+00+a0-", "")
