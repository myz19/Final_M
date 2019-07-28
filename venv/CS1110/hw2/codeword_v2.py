import collections, random  # import modules to be able to use

class crosswordCell:
    def __init__(self, value="_", left=None, right=None, up=None, down=None):   # constructor
        self.value = value
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.neighbors = []
        self.directions = []
        if self.value == None:
            self.full = False
        else:
            self.full = True

    def __str__(self):      # overrides __str__ to just return self.value
        return self.value

    def addNeighbors(self, neighbor, direction):    # add the neighbors and directions of its neighbors into its corresponding lists
        self.neighbors.append(neighbor)
        self.directions.append(direction)

    def isFull(self):       # whether a cell is full or not
        return self.full

class crossword(object):    # creates a class
    def __init__(self, height = 10, width = 10):    # make it 10x10 default
        self.myHeight = height
        self.myWidth = width
        self.data = [[crosswordCell() for _ in range(width)] for _ in range(height)]    # data is all the values in the crossword

    def __str__(self):      # overrides an already known function
        result = []
        for row in self.data:
            for column in row:
                result.append(str(column))      # append all the values to result list
            result.append("\n")
        return "".join(result)      # return the list as a string

    def assignValue(self, index, value):    # assigns a value at a specific index
        x,y = index
        temp = crosswordCell(value)
        self.data[x][y] = temp

    def getCell(self, index):       # gets the cell at a specific index
        x,y = index
        temp = self.data[x][y]
        return temp

    def getCellValue(self, index):      # gets the value of the cell at a specific index
        x, y = index
        temp = self.data[x][y]
        return temp.value

    def setHeight(self, height):    # sets the height (not default)
        self.myHeight = height

    def setWidth(self, width):      # sets the width (not default)
        self.myWidth = width

def getFile():          # function that gets a file with a crossword in it
    print("Enter a file name: ")
    file = input()
    with open(file, 'r') as myFile:
        height = len(myFile.readlines())        # find the height of the crossword
        myFile.seek(0)      # starts at the beginning of the file
        width = len(myFile.readline())          # find the width of the crossword
        myFile.seek(0)
        myCrossword.setHeight(height)       # using functions defined in crossword class
        myCrossword.setWidth(width)
        # print(height, width)
        for no, line in enumerate(myFile):      # for loop and enumerate to iterate over the index and go through each line
            # print(line)
            for num, letter in enumerate(line.rstrip()):    # for loop and enumerate to go through each letter in each line
                # print(no, " ", num, " ", letter)
                myCrossword.assignValue((no, num), letter)      # calls the function from the crossword class
    # print(myCrossword)


def giveClue():
    # creates a dictionary
    dic = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
           'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20',
           'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', '_': '_', '*': '*'}
    print("Your clues: ")
    # prints three clues
    for x in range(3):
        randKey = random.choice(list(dic))      # randomly pick a key
        print("The key is " + randKey + " which is replaced by " + dic[randKey])    # dic[randKey] gives the value at that key

def scramble(char):
    dic = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
           'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20',
           'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', '_': '_', '*': '*'}

    return dic[char]    # exchanges the value and the key for some char

def scrambleCrossword(crossword):
    for rowNumber, row in enumerate(crossword.data):    # for each row
        for colNumber, column in enumerate(row):        # for each column
            # uses the assignValue function to change the letters in the crossword to numbers corresponding in the dictionary
            crossword.assignValue((rowNumber,colNumber), scramble(str(crossword.getCellValue((rowNumber, colNumber)))))
            # print(rowNumber, " ", colNumber)

myCrossword = crossword()

# creates a menu
ans = True
while ans:
    # has to have a file with a crossword already
    print('''
    1. Use a file to create the crossword
    2. Use a file to create the codeword
    3. Exit/Quit''')

    ans = input("What would you like to do? ")

    if ans == "1":
        print("You selected option 1.")
        ans = False
        getFile()
        print(myCrossword)
    elif ans == "2":
        print("You selected option 2.")
        ans = False
        getFile()
        scrambleCrossword(myCrossword)
        print(myCrossword)
        giveClue()
    elif ans == "3":
        print("You selected option 3.")
        ans = False
    else:
        print("Unknown option selected")