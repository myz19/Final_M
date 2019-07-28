from fractions import Fraction      # imports the Fraction module to be able to use it
print("Please enter a list of numbers (with commas between each number): ")   # asks the user to enter a list of numbers with commas in between each number
L=input().split(",")   # puts the inputs into a list
print(L)
mean=0   #initializes average and sum
sum=0

num_list = []   # initializes new list
for x in L:
    if '.' in x and 'e' in x:       # if the number is in scientific notation
        temp = x.split("e")
        num_list.append(float(temp[0]) * (10 ** int(temp[1])))
    elif '.' in x:      # if the number is a decimal (float)
        num_list.append(float(x))
    elif '/' in x:      # if the number is a fraction
        # temp=x.split("/")
        # num_list.append(int(temp[0])/int(temp[1]))
        num_list.append(Fraction(x))    # uses Fraction to be able to print the fraction with a division sign instead of evaluating the fraction
    else:       # if the number is an int
        num_list.append(int(x))

for num in num_list:   # find the sum of the list of numbers
    sum += num

mean = sum/len(num_list)    # find the average of the list of numbers

print("The sum of the list of numbers is " + str(sum) + ".")      # prints the value of sum
print("The average of the list of numbers is " + str(mean) + ".")     # prints the value of mean

minimum = maximum = num_list[0]    # sets the min and max to be the first number in the list
for i in num_list[1: ]:    # compares each value in the list to min and max to determine a new min or max
    if i < minimum:
        minimum = i
    elif i > maximum:
        maximum = i

print("The minimum value of the list of numbers is " + str(minimum) + ".")    # prints the value of min
print("The maximum value of the list of numbers is " + str(maximum) + ".")    # prints the value of max

sumOfVariances = 0      # initializes the value of sumOfVariances
for j in num_list:     # for each value in the list we are going to find the variance and add it to the sumOfVariances
    sumOfVariances += ((j - mean) ** 2)

divide = sumOfVariances/len(L)      # divides the sumOfVariances by the number of numbers in the list
std = divide ** 0.5       # takes the square root to find the value of standard deviation

print("The standard deviation of the list of numbers is " + str(std) + ".")       # prints the value of standard deviation