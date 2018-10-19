# Edit below to select which version to test

#Findings:
#longest2 fails when there are mostly Ds.
#longest3, 4, 5, 6 fails when there is only a longest run of 1.
#longest is the correct one.


from longest import longest_run
#from longest2 import longest_run
#from longest3 import longest_run
#from longest4 import longest_run
#from longest5 import longest_run
#from longest6 import longest_run


def test_longest_run(arg, expected):
    '''
    Checks result for longest_run
    '''
    actual = longest_run(arg)
    if expected != actual:
        print("ERROR: longest_run(" + str(arg) + ")")
        print("Expected:", expected, "Actual:", actual)


# longest run is unique and is in middle of string
print(test_longest_run("abbbccccdddddd", "dddddd"))
print(test_longest_run("abababacdcdcdcd", "a"))