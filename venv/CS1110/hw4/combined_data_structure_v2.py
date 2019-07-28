from __future__ import annotations
from uuid import uuid4
from typing import Dict, List, Set

class Person:
    def __init__(self, name):
        self.uid = uuid4()
        self.rank = 0
        self.name = name

    def __str__(self):      # string representation of a person object
        return f"Person<{self.name}, {self.uid}, {self.rank}>"

class Node:
    def __init__(self, val: Person):        # the node contains a Person
        self.left = None
        self.right = None
        self.next = None
        self.val = val

    def get(self):
        return self.value

    def set(self, val):
        self.val = val

class Town:
    def __init__(self, name, current_population):      # the town is a queue
        self.name = name
        self.uid = uuid4()
        self.population = current_population
        self.head = None
        self.last = None

    def enqueue(self, val):     # adds a node at the end of the queue
        if self.last is None:
            self.head = Node(val)
            self.last = self.head
            val.rank = 0
        else:
            self.last.next = Node(val)
            self.last = self.last.next
            val.rank = self.population
            self.population += 1

    def dequeue(self):      # returns and deletes the first node
        if self.head is None:
            return None
        else:
            head = self.head.val
            self.head = self.head.next
            for i in range(self.population):
                self.head.next = self.head.next.next
                self.head.next.val.rank -= 1
            self.population -= 1
            return head

class BST:      # creates a binary search tree
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val: Person):     # inserts nodes containing People by their uid using recursion
        if val.uid <= currentNode.val.uid:
            if currentNode.left is not None:
                self.insertNode(currentNode.left, val)
            else:
                currentNode.left = Node(val)
        elif val.uid > currentNode.val.uid:
            if currentNode.right is not None:
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):       # finds people using binary search by their uid using recursion
        if currentNode is None:
            return False
        elif val.uid == currentNode.val.uid:
            return currentNode.val
        elif val.uid < currentNode.val.uid:
            return self.findNode(currentNode.left, val)
        else:
            return self.findNode(currentNode.right, val)

if __name__ == "__main__":
    michelle = Node(Person("michelle"))
    jack = Node(Person("jack"))
    sadie = Node(Person("sadie"))

