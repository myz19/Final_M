# works if enters integers
L=[]
print("How many integers would you like to enter? ")
count=int(input())

for reading in range(count):    # assuming count>0
    print("Please enter a integer: ")
    num = input()
    L.append(int(num))      # assuming they put in integers
print(L)

sum=0
for x in L:
    sum+=x
mean=sum/count

print("The sum of the list of integers is " + str(sum))
print("The mean of the list of integers is " + str(mean))

min = max = L[0]    # sets the min and max to be the first number in the list
for i in L[1: ]:    # compares each value in the list to min and max to determine a new min or max
    if i<min:
        min=i
    elif i>max:
        max=i

print("The minimum value of the list of integers is " + str(min))    # prints the value of min
print("The maximum value of the list of integers is " + str(max))    # prints the value of max

sumOfVariances = 0      # initializes the value of sumOfVariances
for j in L:     # for each value in the list we are going to find the variance and add it to the sumOfVariances
    sumOfVariances += float(((j-mean)**2))
divide = sumOfVariances/len(L)      # divides the sumOfVariances by the number of numbers in the list
std = divide**0.5       # takes the square root to find the value of standard deviation

print("The standard deviation of the list of integers is " + str(std))       # prints the value of standard deviation
