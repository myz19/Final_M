from random import randint

def makeRandomName():
    consonants = ("b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")
    vowels = ("a", "e", "i", "j", "o", "u", "y")
    length = randint(3, 7)  ## length of the name
    myname = ""  # start with an empty string
    ### print("...about to start in random names")
    for location in range(length):
        pick = randint(1, 2)
        ##print("pick = " +str(pick))
        if pick == 1:
            letter = consonants[randint(0, len(consonants) - 1)]
        if pick == 2:
            letter = vowels[randint(0, len(vowels) - 1)]
        myname += letter
    return myname

####+++++++++++++++++++++++++++++
class peepy :

    numMade = 0  ## this is a class variable rather than a variable belonging to the object
    # have to call it from the class peepy.numMade

    def __init__(self, name="anon", age=-1):
        if name == "anon":
            self.myname = makeRandomName()
        else:
            self.myname = name
        if age == -1:
            self.myage = randint(0,150)
        else:
            self.myage = age
        self.ID = peepy.numMade
        peepy.numMade += 1 ## incrementing the number made

    def getName(self):
        return self.myname

    def setName(self, nom):
        self.myname = nom

    def showAge(self):
        return self.myage

    def displayPeep(self):
        return self.myname + "(" + str(self.myage) + ")"