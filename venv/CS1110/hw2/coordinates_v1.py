print("Enter how many more coordinate points you would like to enter: ")    # asks the user for how many coordinates
no_of_points = int(input())

points_list = []    # initializes empty lists for all the points, then for the ones that are above, below, and on the line
above = []
below = []
on = []

print("Enter the additional coordinate points (one per line with no parentheses): ")
for x in range(no_of_points):   # add each coordinate point to the list
    a = input().split(",")      # splits each coordinate to an x and y value
    points_list.append((float(a[0]), float(a[1])))      # can input decimals or integers

    if (float(a[0]) == float(a[1])):        # puts each coordinate into a new list whether they are on, above, or below the line
        on.append((float(a[0]), float(a[1])))
    elif (float(a[0]) > float(a[1])):
        below.append((float(a[0]), float(a[1])))
    elif (float(a[0]) < float(a[1])):
        above.append((float(a[0]), float(a[1])))

print(points_list)
list_of_tuples = [("above", len(above)), ("below", len(below)), ("on", len(on))]        # creates a list of tuples with the list and its length

list_of_tuples.sort(key = lambda x: x[1], reverse = True)       # sorts the list of tuples based on the length

print(list_of_tuples)

print(list_of_tuples[0][0] + " > " + list_of_tuples[1][0] + " > " + list_of_tuples[2][0])       # prints the comparison

