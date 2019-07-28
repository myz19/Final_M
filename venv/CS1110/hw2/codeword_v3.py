import collections, random  # import modules to be able to use

class crosswordCell:
    def __init__(self, value="_"):   # constructor
        self.value = value
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def __str__(self):      # overrides __str__ to just return self.value
        return self.value

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

    '''def addCell(self, index, cell):
        row, col = index
        if row > 1 and col > 1:
            print("We don't support adding cell for a crossword bigger than one cell.")
        self.data[row][col] = cell'''

    '''def updateCellRelationship(self):       # what cell neighbors are avaiable
        for row in range(self.myHeight-1, 0, -1):
            for col in range(self.myWidth-1, 0, -1):
                if row < 1 or col < 1 or row > self.myHeight-1 or col > self.myWidth-1:
                    break
                elif row == self.myHeight-1 and col == self.myWidth-1:    # bottom right corner
                    self.data[row][col].up = self.data[row-1][col]
                    self.data[row][col].left = self.data[row][col-1]
                elif row == self.myHeight-1 and col == 0:   # bottom left corner
                    self.data[row][col].up = self.data[row - 1][col]
                    self.data[row][col].right = self.data[row][col + 1]
                elif row == self.myHeight-1 and 0<col<self.myWidth-1:   # bottom row
                    self.data[row][col].up = self.data[row - 1][col]
                    self.data[row][col].left = self.data[row][col - 1]
                    self.data[row][col].right = self.data[row][col + 1]
                elif row == 0 and col == 0:     # top left corner
                    self.data[row][col].right = self.data[row][col + 1]
                    self.data[row][col].down = self.data[row+1][col]
                elif row == 0 and col == self.myWidth-1:    # top right corner
                    self.data[row][col].down = self.data[row + 1][col]
                    self.data[row][col].left = self.data[row][col - 1]
                elif row == 0 and 0<col<self.myWidth-1: # top row
                    self.data[row][col].left = self.data[row][col - 1]
                    self.data[row][col].right = self.data[row][col + 1]
                    self.data[row][col].down = self.data[row + 1][col]
                elif col == 0 and 0<row<self.myHeight-1:    # left column
                    self.data[row][col].right = self.data[row][col + 1]
                    self.data[row][col].down = self.data[row + 1][col]
                    self.data[row][col].up = self.data[row - 1][col]
                elif col == self.myWidth - 1 and 0<row<self.myHeight-1:     # right column
                    self.data[row][col].down = self.data[row + 1][col]
                    self.data[row][col].up = self.data[row - 1][col]
                    self.data[row][col].left = self.data[row][col - 1]
                else:   # everything else in the middle
                    self.data[row][col].down = self.data[row + 1][col]
                    self.data[row][col].up = self.data[row - 1][col]
                    self.data[row][col].left = self.data[row][col - 1]
                    self.data[row][col].right = self.data[row][col + 1]'''

    def insertWord(self, index, direction, word):       # what position to insert and what direction
        row,col = index    # tuple
        if direction == 'down':         # makes sure the word length is shorter than or equal to the height of the crossword from the index
            if len(word) > (self.myHeight - row):
                print('The word is too long, please use a shorter word.')
            else:
                for row1 in range(row, row + len(word), 1):
                    self.data[row1][col] = crosswordCell(value= word[row1 - row])   # makes sure the index starts with 0 for the actual word
        if direction == 'cross':        # makes sure the word length is shorter than or equal to the width of the crossword from the index
            if len(word) > (self.myWidth - col):
                print('The word is too long.')
            else:
                for col1 in range(col, col + len(word), 1):
                    self.data[row][col1] = crosswordCell(value= word[col1 - col])

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
    3. Insert word for crossword 
    4. Exit/Quit''')

    ans = input("What would you like to do? ")

    if ans == "1":
        print("You selected option 1.")
        ans = False
        getFile()
        print(myCrossword)
        myCrossword.updateCellRelationship()
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
        print("Enter a position, direction (down or cross), and word separated by semicolons.")     # tells the user how to enter
        position_list = input("Enter position (with no parenthesis): ").split(",")      # splits the position into x and y values
        position = (int(position_list[0]), int(position_list[1]))       # makes it a tuple
        direction = str(input("Enter direction: "))
        word = str(input("Enter the word: "))
        myCrossword.insertWord(position, direction, word)       # calls the function
        print(myCrossword)
    elif ans == "4":
        print("You selected option 4.")
        ans = False
    else:
        print("Unknown option selected")