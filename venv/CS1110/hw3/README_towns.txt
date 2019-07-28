I created a class called Person and in its constructor it has a name, id, set of friends, and set of mutual friends.
I overrode the __str__ function to print out the person's name and id as the string representation of a Person. I created
a function called addFriend that takes a person and adds it to self's set of friends. But it also checks if they are
mutual friends and if they are, the function adds each person in their respective set of mutual friends. The function
getMutualFriends just returns the set of mutual friends. The function isMutual checks if two people are mutual by checking
if their id's are in the other person's set of friends. I then created a class called Town. The __init__ function
has the town's name, id, maxCapacity, currentPopulation, olimit, and ilimit and sets of citizens, outgoing and incoming
roads. The __contains__ function changes the function of the word "in" in the person in town function. The function getCitizens
just returns the list of all the citizens in a town. Then addCitizen adds the person into the set and adds one to the population.
removeCitizen checks first if the person is in the town that they want to be removed from and then removes the person
and subtracts one from the population of that town. If the person is not in the town it raises an error. I also wrote a
function to check that there is enough space in the town to add more people since each town has a maxCapacity. I created
an exception that happens when a person is not in a town. I created a class called Map. Its init function creates
a dictionary with the key as each town and its value as the set of all the towns it directly points to (adjacent towns).
getTowns returns the list of all of the towns by going through each key in the dictionary. get_town_of_person finds the
town a person is in by looking through the set of all the towns and checking if that person is in the citizens set.
move_person takes in a person and a destination. It first finds the town the person is currently in and then checks if
the destination town has enough space to add another person. Then it adds the person to the destination and removes the
person from the current town they were at. Then to get the friends to alert I found the intersection of the destination
citizens and the mutual friends list of the person and alerted those people that their friend was coming. Then to alert
friends that the person was leaving I found the intersection of the citizens in the current town and the mutual friends
list.

