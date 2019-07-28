print("Enter how many more coordinate points you would like to enter: ")    # asks the user for how many coordinates
no_of_points = int(input())

points_list = []    # initializes empty lists for all the points, then for the ones that are above, below, and on the line
above = []
below = []
on = []

print("Enter the additional coordinate points (one per line with no parentheses): ")

def determinePoints(tuple_point):       # creates a function to determine which list the coordinate goes into
    if (float(tuple_point[0]) == float(tuple_point[1])):
        on.append((float(tuple_point[0]), float(tuple_point[1])))
    elif (float(tuple_point[0]) > float(tuple_point[1])):
        below.append((float(tuple_point[0]), float(tuple_point[1])))
    elif (float(tuple_point[0]) < float(tuple_point[1])):
        above.append((float(tuple_point[0]), float(tuple_point[1])))

for x in range(no_of_points):   # enters the coordinates
    a = input().split(",")      # splits the coordinates into x and y value
    points_list.append((float(a[0]), float(a[1])))      # add the tuple to points_list
    determinePoints((float(a[0]), float(a[1])))         # uses the new function to determine where the point goes to

with open('coordinates.txt', 'r') as my_file:       # reads a file with coordinates already in it
    for line in my_file:        # reads each line (each coordinate)
        b = line.replace("\n", "").split(",")   # splits each coordinate into x and y value
        # print(b)
        determinePoints((float(b[0]), float(b[1])))     # uses function to put into a list

print(points_list)
list_of_tuples = [("above", len(above)), ("below", len(below)), ("on", len(on))]        # creates a list of tuples with the list and its length

list_of_tuples.sort(key = lambda x: x[1], reverse = True)       # sorts the list of tuples based on the length

print(list_of_tuples)

print(list_of_tuples[0][0] + " > " + list_of_tuples[1][0] + " > " + list_of_tuples[2][0])       # prints the comparison

with open('list_of_tuples.txt', 'w') as l:      # creates a new file to write in
    l.write(str(on))        # puts in the on list
    l.write('\n')           # new line
    l.write(str(above))     # puts in the above list
    l.write('\n')           # new line
    l.write(str(below))     # puts in the below list

with open('list_of_tuples.txt', 'r') as my_lists:       # read the new file
    on = my_lists.readline().rstrip()       # reads the first line removing the trailing characters and assign it to on
    above = my_lists.readline().rstrip()    # reads the next line removing the trailing characters and assign it to above
    below = my_lists.readline().rstrip()    # reads the next line removing the trailing characters and assign it to below

print("on:", on)        # prints each list
print("above:", above)
print("below:", below)
