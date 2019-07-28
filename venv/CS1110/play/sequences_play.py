'''niceList = []

niceList.append("sausage")
niceList.append(("rhubarb", 256))   # appended a tuple
niceList.append([37, "yummyness", "kangaroos"])
niceList.append(niceList)       # printed out a ... as the next element in the list

print("list length = " + str(len(niceList)))
print(niceList)'''

myList = [(x**2,y) for x in range(5) for y in range(4)]
tempList = []
hisList = []    # to hold a bunch of integers entered at the keyboard

print("how many numbers would you like to give me? ")
count=int(input())
print("you told me you'd like to count " + str(count) + " things.")

for reading in range(count):    # assuming count>0
    print("Please enter an integer: ")
    blah = input()
    hisList.append(int(blah))   # trusting that they entered an integer
print(hisList)

total=0
for x in hisList:
    total+=x
print("The sum of all those integers = " + str(total))

# let's make a list of all the y-values in myList
y_values=[]
for tuply in myList:
    if tuply[1] not in y_values:
        y_values.append(tuply[1])
print("so the list of y values = " + str(y_values) + "\n")

for y in y_values:
    for tuply in myList:
        if tuply[1]  == y:
            tempList.append(tuply)
    print(tempList)
    tempList.clear()

'''print("myList has " + str(len(myList)) + " things in it, and myList = \n\t"+ str(myList))
print()
print("more prettily, myList = \n")
for tuply in myList:
    if tuply[1]==0:
        print(str(tuply) + ", ")
print("\n")
for tuply in myList:
    if tuply[1]==1:
        print(str(tuply) + ", ")
print("\n")
for tuply in myList:
    if tuply[1]==2:
        print(str(tuply) + ", ")
print("\n")
for tuply in myList:
    if tuply[1]==3:
        print(str(tuply) + ", ")
print("\n")'''

for tuply in myList:
    if tuply[1]==0:
        yourList.append(tuply)
print(yourList)
yourList.clear()
for tuply in myList:
    if tuply[1]==1:
        yourList.append(tuply)
print(yourList)
yourList.clear()
for tuply in myList:
    if tuply[1]==2:
        yourList.append(tuply)
print(yourList)
yourList.clear()
for tuply in myList:
    if tuply[1]==3:
        yourList.append(tuply)
print(yourList)
yourList.clear()

