For the first version I just copied my homework from the previous week about towns and deleted some stuff
about friends and mutual friends. Then I added a rank value for the Person class and set it equal to 0. Then I created
a isEmpty() function to see if the town is empty. Then if the town is empty the rank of the person who is added
is 0. Then every other time the rank is equal to the town population. When removing a person (since its only from the
front) the all the other persons ranks in the town will be subtracted by one. Then I also created a searchByRank method
to do binary search on each town to look for a specific person by their rank since their town rank is already sorted
since they are the order of where they are in the queue. Since I have the searchByRank method in a class I couldn't use
it recursively.

For the second version I created a Person class and a Person object which as a name, uid, and rank. Then I overrode the
__str__ method to say how the string representation of Person should look like. Then I created a class called Node
to be able to make and use queues and binary search trees. The Node had a parameter called value that would contain a
Person. The Node also has left and right values for the binary search trees and a next value for the queue. Then I added
a getter and setter method for the value of the Node. I then created a class called Town that works like a queue but in
the constructor it has a name, uid, and population value. Then I also added a head and a last node that is initialized to
None for the queue. I created a function called enqueue that adds a node to the end of the queue. It checks if the last
value in the queue = None (if the queue is empty) and makes the head the node that is being inserted and makes that also
equal to the last node. Then I made the rank of the Person in the Node equal to 0 since it is the first Person. If this
isn't the case then that means there are nodes in the queue so the last node would now be the node I am adding into the
queue. Then I set the person's rank in the node to the population of the town and added one to the population of the
town. Then I created a function called dequeue that deletes the first node of the queue since that's the only way of
removing a node from a queue. It first checks if the head node is None cause if it is then that means there's nothing
in the queue and nothing to delete. If not, the head is the next value of the node that is being removed. Then I tried
to change the rank of the people in the queue to subtracting one from each person. But since this is not a list or set
I'm not sure if I did it properly. I created a BST class for the binary search tree. In the constructor there is only a
root that is initialized to None. Then I created an insert function to first check if the tree is empty and if not it called
another function called insertNode. insertNode is recursive and inserts the Node containing the Person by their uid. If
it is less than or equal to then it is inserted as a left child and if its greater its inserted as a right child. Then
I created a find function that first checks if the tree is empty or else it calls a findNode function which is recursive
and checks by uid. If the uids are equal I just return the current node and the Person in the node if less than, I go left
and if it's greater than I go right. It goes through it recursively until it finds the Node(person) that it is looking for.
