# inherit exceptions and make it our own
# to inherit after your class name in parenthesis you put the class name that you are inheriting from (same as extend in java)

class NotFoundException(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class AtFrontException(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class EmptyException(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class OnlyOneThingException(Exception):
    def __init__(self, value):
        self.value = [value, " has only one thing in it"]
    def __str__(self):
        return repr(self.value)

class OnlyTwoThingsException(Exception):
    def __init__(self, value):
        self.value = [value, " has only two things in it"]
    def __str__(self):
        return repr(self.value)

class OnlyFinitelyManyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def printList(goofy):
    print(goofy)
    try:        # possibility that there might be an exception thrown from there
        if len(goofy) == 0:
            raise EmptyException("it's empty :(")
        elif len(goofy) == 1:
            raise OnlyOneThingException(goofy)
        elif len(goofy) ==2:
            raise OnlyTwoThingsException(goofy)
        else:
            raise OnlyFinitelyManyException(len(goofy))
            print("My list only had finitely many things in it.")
    except EmptyException as ee:        # if something crazy happened that is not thought about above
        print()

