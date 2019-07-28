from __future__ import annotations
import random
import numpy as np

class Matrices:
    def __init__(self, array):      # constructor with a parameter array
        self.array = array

    def addRows(self, row1, row2, multiple1, multiple2):        # add two different rows with each row being multiplied by a multiple
        self.array[row1] = [x*multiple1 + y*multiple2 for x, y in zip(self.array[row1], self.array[row2])]   # makes the addition of the rows equal to the first row number parameter

    def __str__(self):      # string representation of a matrix
        result = []
        for row in self.array:
            for column in row:
                result.append(str(column) + " ")  # append all the values to result list
            result.append("\n")
        return "".join(result)

    def __getitem__(self, x):       # accessing list items, will be called twice for [x][y]
        return self.array[x]

    def appendVector(self, vector: Vectors, direction: str):        # add vector to the end
        if len(self.array) == 1 and len(self.array[0]) == 0:        # if empty
            self.array.append(vector.array)
            del self.array[0]
        else:
            if direction == "column" and len(vector.array) > len(self.array):       # if different column length
                print("Cannot append a different column length vector.")
            elif direction == "column" and len(vector.array) == len(self.array):    # have to append one value at a time
                for no, row in enumerate(self.array):
                    row.append(vector.array[no][0])
            elif direction == "row" and len(vector.array) > len(self.array[0]):     # if different row length
                print("Cannot append a different row length vector.")
            elif direction == "row" and len(vector.array) == len(self.array[0]):    # append at the end
                self.array.append(vector.array)

class Vectors:
    def __init__(self, array, direction: str):
        self.array = array
        self.direction = direction
        if direction == "column" and len(self.array[0]) > 1:        # make sure it is a vector, don't need one for if direction is row
            print("This is not a vector. Please try again.")

def solveSystems(matrix: Matrices):             # uses the addRows function to solve a system of equations
    if matrix.array[0][0] != 0:     # checks division by 0
        matrix.addRows(1,0,1,-((float(matrix.array[1][0]))/(float(matrix.array[0][0]))))        # gets zeros in the first column, 2nd and 3rd rows
        matrix.addRows(2,0,1,-(float(matrix.array[2][0])/float(matrix.array[0][0])))
    else:
        print("Error: division by 0!")
    if matrix.array[1][1] != 0:
        matrix.addRows(2,1,1,-((float(matrix.array[2][1]))/(float(matrix.array[1][1]))))        # gets a zero in the second column, third row
    else:
        print("Error: division by 0!")
    if matrix.array[2][2] != 0:
        matrix.addRows(0,2,1,-(float(matrix.array[0][2])/float(matrix.array[2][2])))        # gets zeros in the first two rows of the third column
        matrix.addRows(1,2,1,-(float(matrix.array[1][2])/float(matrix.array[2][2])))
    else:
        print("Error: division by 0!")
    if matrix.array[1][1] != 0:
        matrix.addRows(0,1,1,-(float(matrix.array[0][1])/float(matrix.array[1][1])))        # gets zero in the second column, first row
    else:
        print("Error: division by 0!")

    a = round(float(matrix.array[0][3]) / float(matrix.array[0][0]),2)      # solves for each variable
    b = round(float(matrix.array[1][3]) / float(matrix.array[1][1]),2)      # rounded to two decimal places to not get huge decimals and so we won't need a function to check if it solves to close enough
    c = round(float(matrix.array[2][3]) / float(matrix.array[2][2]),2)

    print("a = " + str(a) + "\n" + "b = " + str(b) + "\n" + "c = " + str(c))
    print("secret = " + str(c))
    return c

def makeSecretAndGiveOutShares():
    m = Matrices([[]])
    y_list = []
    a = round(random.randint(0,100)/10, 2)      # creates random values of a, b, c for the matrix to solve for
    b = round(random.randint(0,100)/10, 2)      # divided by 10 to get decimals
    c = round(random.randint(0,100)/10, 2)
    print("The correct values of a, b, c are : ", a, b, c, "respectively.")
    secret = c
    for no in range(3):     # random values for x
        x = round(random.randint(0,100)/10,2)
        # print(x)
        v = Vectors([round(x,2)**2, x, 1], "row")       # adds each vector to make a 3x3
        m.appendVector(v, "row")
        # print(m)
        y = [a*(x**2) + b*x + c]    # uses random x value to get the y value and then you have three random coordinates to use to solve the system of equations
        y_list.append(y)        # y value vector
    # print(y_list)
    vy = Vectors(y_list, "column")
    m.appendVector(vy, "column")        # adds the last column
    print(m)
    return m

myMatrix = makeSecretAndGiveOutShares()
solveSystems(myMatrix)

