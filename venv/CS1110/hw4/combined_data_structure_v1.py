from __future__ import annotations
from uuid import uuid4
from typing import Dict, List, Set

class Person:
    def __init__(self, name: str):
        self.uid = uuid4()          # guarantees unique id
        self.name = name
        self.rank = 0

    def __str__(self):      # string representation of a person object
        return f"Person<{self.name}, {self.uid}, {self.rank}>"

    def get_name(self):     # gets the name of the person in a function
        return self.name


class Town:
    def __init__(self, name: str, maxCapacity: int, currentPopulation: int, olimit: int, ilimit: int):
        self.name = name
        self.uid = uuid4()
        self.capacity = maxCapacity
        self.population = currentPopulation
        self.citizens = list()
        self.outgoing_roads = set()
        self.incoming_roads = set()
        self.outgoing_limit = olimit
        self.incoming_limit = ilimit

    def __contains__(self, person: Person) -> bool:   # if person in town will run this function
        return person in self.citizens      # makes sure it checks in citizens instead of checking all of the variables

    def __getitem__(self, x):
        return self.citizens[x]

    def isEmpty(self):
        if self.population == 0:
            return True
        else:
            return False

    def hasEnoughSpace(self):       # checks if there is enough space to add someone since each town has a max capacity
        if self.population < self.capacity:
            return True
        elif self.population == self.capacity:
            return False

    def getCitizens(self):
        """Return the citizens."""
        return self.citizens

    def addCitizen(self, person: Person):
        """Adds a person to a town"""
        if self.hasEnoughSpace():
            self.citizens.append(person)
            self.population += 1
            if self.isEmpty():
                person.rank = 0
            else:
                person.rank = self.population

    def removeCitizen(self, person: Person):
        """Removes a person from the town."""
        if person in self.citizens:
            if person.rank == 0:
                self.citizens.remove(person)
                self.population -= 1
                for p in self.citizens:
                    p.rank -= 1
            return
        raise KeyError      # if person not in town

    def searchByRank(self, person):     # searches by the rank of the person using binary search
        first = 0
        last = len(self.citizens)-1
        found = False

        while first<=last and not found:
            midpoint = (first+last)//2
            q = self.citizens[midpoint]
            if q.rank == person.rank:
                found = True
            else:
                if person.rank < q.rank:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found


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
            person.rank = destination.population


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

    map.move_person(michelle, town2)
    town1.searchByRank(michelle)
