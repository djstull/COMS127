#This program is just a simple way for me to practice functions.
def nicememe():
    meme = input("What's the best meme on the planet?")
    if meme in ["we are number one"]:
        print("HA HA HA, Now look at this net, that I just found, when I say go, be ready throw.")
        print("GO")
        whothrown = ("Do you throw it on him or robbie?: ")
        if whothrown in ["robbie"]:
            print("Throw it on him not me! Ugh, let's try something else.")
        elif whothrown in ["him"]:
            print("A HA HA")
        else:
            print("You dropped the net!")
nicememe()