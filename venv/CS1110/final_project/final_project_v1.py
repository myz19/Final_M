class Person:
    def __init__(self, name):
        self.name = name
        self.uid = uuid4()
        self.friends = set()
        self.mutual_friends = set()

class Country:
    def __init__(self):
        pass

class Map:
    def __init__(self):
        pass

