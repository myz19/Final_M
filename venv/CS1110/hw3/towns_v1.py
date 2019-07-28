from __future__ import annotations
from uuid import uuid4
from typing import Dict, List, Set

class Person:
    def __init__(self, name: str):
        self.uid = uuid4()          # guarantees unique id
        self.name = name
        self.friends = set()        # each object as a unique identifier
        self.mutual_friends = set()

    # def __repr__(self):
    #     return f"Person<{self.name}>"

    def __str__(self):      # string representation of a person object
        return f"Person<{self.name}, {self.uid}>"

    def get_name(self):     # gets the name of the person in a function
        return self.name

    def addFriend(self, person: Person, is_mutual: bool = False):
        """Add a friend to set of friends"""
        self.friends.add(person)
        if is_mutual:       # checks if mutual friends
            person.friends.add(self)
        if self in person.friends:      # then adds to mutual friends list of each person
            self.mutual_friends.add(person)
            person.mutual_friends.add(self)

    # def getMutualFriendsAsString(self):
    #     """Returns a string representing mutual friends of the current person."""
    #     content = f"{self.name}'s mutual friends list"
    #     content += f"\n{len(content) * '-'}"
    #     for friend in self.mutual_friends:
    #         content += f"\n{friend.name}"
    #     return content

    def getMutualFriends(self)-> Set[Person]:
        """Returns the set of mutual friends."""
        return self.mutual_friends

    def isMutual(self, person: Person):
        """Returns true if two people are mutual friends"""
        return self.uid in person.friends and person.uid in self.friends        # checks by id

class Town:
    def __init__(self, name: str, maxCapacity: int, currentPopulation: int, olimit: int, ilimit: int):
        self.name = name
        self.uid = uuid4()
        self.capacity = maxCapacity
        self.population = currentPopulation
        self.citizens = set()
        self.outgoing_roads = set()
        self.incoming_roads = set()
        self.outgoing_limit = olimit
        self.incoming_limit = ilimit

    def __contains__(self, person: Person) -> bool:   # if person in town will run this function
        return person in self.citizens      # makes sure it checks in citizens instead of checking all of the variables

    def getCitizens(self) -> Set[Person]:
        """Return the citizens."""
        return self.citizens

    def addCitizen(self, person: Person):
        """Adds a person to a town"""
        self.citizens.add(person)
        self.population += 1

    def removeCitizen(self, person: Person):
        """Removes a person from the town."""
        if person in self.citizens:
            self.citizens.remove(person)
            self.population -= 1
            return
        raise KeyError      # if person not in town

    def hasEnoughSpace(self):       # checks if there is enough space to add someone since each town has a max capacity
        if self.population < self.capacity:
            return True
        elif self.population == self.capacity:
            return False

class NotInAnyTown(Exception):      # creates my own exception
    pass

class Map:
    def __init__(self, map_as_dict: Dict[Town, Set[Town]]):
        self.towns: Dict[Town, Set[Town]] = map_as_dict     # makes a dictionary with key as each town and value as all the towns the key points to

    def get_towns(self) -> List[Town]:
        """Returns a list of towns."""
        towns = list(self.towns.keys())
        return towns

    def get_town_of_person(self, person: Person, towns: List[Town]):
        """Find the town the person is in"""
        for town in towns:
            if person in town:
                return town
        raise NotInAnyTown

    def move_person(self, person: Person, destination: Town):
        towns = self.get_towns()        # gets list of towns
        town_of_person = self.get_town_of_person(person, towns)     # gets the town the person is in
        if destination.hasEnoughSpace():        # checks if there is enough space to add
            town_of_person.removeCitizen(person)
            destination.addCitizen(person)
        # check the intersection of that town's citizens with the mutual friends list of that person
        mf = person.getMutualFriends()
        friends_to_alert = mf.intersection(destination.getCitizens())
        friends_to_unalert = mf.intersection(town_of_person.getCitizens())

        for fr in friends_to_alert:
            self.alert_friends(f"Hey {fr.get_name()}, I'm coming to your town!")

        for fr in friends_to_unalert:
            self.alert_friends(f"Sorry {fr.get_name()}, I have to go!")

    def alert_friends(self, msg):
        """Alerts a friend of arriving or leaving their town."""
        print(msg)



if __name__ == "__main__":
    michelle = Person("Michelle")
    jack = Person("Jack")
    kyle = Person("Kyle")
    wenyi = Person("Wenyi")
    darian = Person("Darian")
    jennifer = Person("Jennifer")

    town1 = Town("Ithaca", maxCapacity=10, currentPopulation =0, olimit=2, ilimit=2)
    town1.addCitizen(michelle)
    town1.addCitizen(darian)
    town1.addCitizen(kyle)
    town1.addCitizen(jack)
    town2 = Town("New York City", maxCapacity=10, currentPopulation =0, olimit=2, ilimit=2)
    town2.addCitizen(jennifer)
    town2.addCitizen(wenyi)

    map = Map({
        town1: {town2},
        town2: {town1}
    })

    michelle.addFriend(jack, is_mutual = True)
    michelle.addFriend(kyle, is_mutual= True)
    michelle.addFriend(jennifer, is_mutual=True)

    map.move_person(michelle, town2)