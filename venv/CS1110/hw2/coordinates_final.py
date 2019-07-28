points_list = []        # initializes empty lists
above = []
below = []
on = []

def determinePoints(tuple_point):       # function to place the coordinates into the correct list
    if (float(tuple_point[0]) == float(tuple_point[1])):
        on.append((float(tuple_point[0]), float(tuple_point[1])))
    elif (float(tuple_point[0]) > float(tuple_point[1])):
        below.append((float(tuple_point[0]), float(tuple_point[1])))
    elif (float(tuple_point[0]) < float(tuple_point[1])):
        above.append((float(tuple_point[0]), float(tuple_point[1])))

def printCoordinates():     # function to print the coordinates and the comparison
    print(points_list)
    list_of_tuples = [("above", len(above)), ("below", len(below)), ("on", len(on))]  # creates a list of tuples with the list and its length

    list_of_tuples.sort(key=lambda x: x[1], reverse=True)  # sorts the list of tuples based on the length

    print(list_of_tuples)

    if list_of_tuples[0][1] == list_of_tuples[1][1] and list_of_tuples[0][1] == list_of_tuples[2][1]:   # if they are all equal
        print(list_of_tuples[0][0] + " = " + list_of_tuples[1][0] + " = " + list_of_tuples[2][0])
    else:
        print(list_of_tuples[0][0] + " > " + list_of_tuples[1][0] + " > " + list_of_tuples[2][0])

def printFile(on, above, below):       # function to print the lists using a file
    with open('list_of_tuples.txt', 'w') as l:  # creates a new file to write in
        l.write(str(on))  # puts in the on list
        l.write('\n')  # new line
        l.write(str(above))  # puts in the above list
        l.write('\n')  # new line
        l.write(str(below))  # puts in the below list

    with open('list_of_tuples.txt', 'r') as my_lists:  # read the new file
        on = my_lists.readline().rstrip()  # reads the first line removing the trailing characters and assign it to on
        above = my_lists.readline().rstrip()  # reads the next line removing the trailing characters and assign it to above
        below = my_lists.readline().rstrip()  # reads the next line removing the trailing characters and assign it to below

    print("on:", on)  # prints each list
    print("above:", above)
    print("below:", below)

def manualInput():      # function to into coordinates manually without a file
    print("Enter how many more coordinate points you would like to enter: ")
    no_of_points = int(input())

    print("Enter the additional coordinate points (one per line with no parentheses): ")

    for x in range(no_of_points):  # enters the coordinates
        a = input().split(",")  # splits the coordinates into x and y value
        points_list.append((float(a[0]), float(a[1])))  # add the tuple to points_list
        determinePoints((float(a[0]), float(a[1])))  # uses the new function to determine where the point goes to

    printCoordinates()      # calls the function that compares
    printFile(on, above, below)     # calls the file that prints the three lists

def readFile():     # function that asks the user to input a file name with coordinates already in it
    print("Enter file name: ")      # asks for the file name
    file = input()
    with open(file, 'r') as my_file:     # reads the file
        for line in my_file:        # for every line
            b = line.replace("\n", "").split(",")       # splits
            # print(b)
            determinePoints((float(b[0]), float(b[1])))     # calls function to put the coordinates into the right list

    printCoordinates()      # calls function that compares the lengths of the lists
    printFile(on,above,below)   # calls function that prints the three lists

ans = True      # creates a menu
while ans:      # different options
    print('''      
    1. Enter the coordinates manually       
    2. Enter a file name with coordinates
    3. Exit/Quit''')

    ans = input("What would you like to do? ")

    if ans == "1":
        print("You selected option 1.")
        ans = False     # stops it from asking the menu again
        manualInput()   # calls function that creates the three lists from manually inputted coordinates
    elif ans == "2":
        print("You selected option 2.")
        ans = False     # stops it from asking the menu again
        readFile()      # calls function that creates the three lists from a file
    elif ans == "3":
        print("You selected option 3.")
        ans = False     # quits
    else:
        print("Unknown option selected")