# works with Python 2

L=list()    # makes L a list
print("Please enter a list of numbers (with commas between each number): ")   # asks the user to enter a list of numbers with commas in between each number
L=input()   # puts the inputs into a list
mean=0   #initializes average and sum
sum=0

for num in L:   # find the sum of the list of numbers
    sum += num
mean = sum/len(L)    # find the average of the list of numbers

print("The sum of the list of numbers is " + str(sum))      # prints the value of sum
print("The average of the list of numbers is " + str(mean))     # prints the value of mean

min = max = L[0]    # sets the min and max to be the first number in the list
for i in L[1: ]:    # compares each value in the list to min and max to determine a new min or max
    if i<min:
        min=i
    elif i>max:
        max=i

print("The minimum value of the list of numbers is " + str(min))    # prints the value of min
print("The maximum value of the list of numbers is " + str(max))    # prints the value of max

sumOfVariances = 0      # initializes the value of sumOfVariances
for j in L:     # for each value in the list we are going to find the variance and add it to the sumOfVariances
    sumOfVariances+=((j-mean)**2)
divide = sumOfVariances/len(L)      # divides the sumOfVariances by the number of numbers in the list
std = divide**0.5       # takes the square root to find the value of standard deviation

print("The standard deviation of the list of numbers is " + str(std))       # prints the value of standard deviation