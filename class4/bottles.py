#This function "sings" a verse of 99 bottles of beer.
#I seriously don't know why we are doing this in class. I'm paying $20,000 for this.
def sing_verse(num):
    print(
        "%s bottles of beer on the wall, %s bottles of beer. Take one down, pass it around, %s bottles of beer on the wall.\n" % (num, num, num-1)
    )
#sets the number of bottles to the verse
bottles = 99

while bottles >= 1:
    sing_verse(bottles)
    bottles = bottles - 1
