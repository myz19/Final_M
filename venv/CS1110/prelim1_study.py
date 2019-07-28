from string import ascii_letters
from random import choice

def problem1():
    # problem 1
    user_input = "not an integer"
    is_negative = False
    while not user_input.isdigit():
        is_negative = False
        user_input = input("Enter an integer: ")
        if user_input[0] == "-":
            user_input = user_input[1:]
            is_negative = True

    if is_negative:
        user_input = -1 * int(user_input)
    else:
        user_input = int(user_input)

    if user_input % 2 == 1:
        print("That's very odd.")
    else:
        evens_file = open("evens.txt", "r")
        print(evens_file.readline())  # readline reads one line, readlines reads all the lines
        evens_file.close()

# problem 4
class LListNode:
    def __init__(self, person, next = None):
        # person should be a person object
        self.data = person
        # next should be a linked list node object
        self.next = next

class LList:
    def __init__(self, node):
        # node should be a linked list node object
        self.head = node

class Person:
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = Person.id
        Person.id += 1

def problem4():
    people = []
    for _ in range(10):
        name = ''.join([choice(ascii_letters) for _ in range(8)])
        person = person(name)
        print(f"Person: {person.name} -- Persons ID: {person.id}")

def above(points, m):
    pointsAboveTheLine = 0
    for tuple in points:
        if tuple[1] > m * tuple[0]:
            pointsAboveTheLine += 1
    return pointsAboveTheLine


if __name__ == "__main__":
    above([(1,2), (2,4), (3,7)], 2)