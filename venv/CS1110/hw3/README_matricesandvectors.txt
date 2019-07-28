I created a Matrices class where the constructor gets an array. For the addRows function I used list comprehension to
multiple each row by a value and add the two rows and set it equal to the first row number parameter. I overrode the
__str__ function to make the string representation of a matrix that would print out when I printed out the matrix. I
overrode the getitem function to fix an error I kept on getting. This helped access the list items and is called twice
since it is a 2d array. I also created appendVector function that adds a row or column vector. If it checks if the
matrix is empty ([[]]). Then it appends the vector and deletes the empty list already there to indicate that the matrix
is empty. Then for every additional vector, it checks the direction and the length in that direction to make sure it
can append it. For column vectors we have to append the values in the vector once at a time to each row. Then I created
a Vector class that only takes in an array and the direction of the vector. It also checks that the array is a vector
by checking if its a length of one based on what direction the vector is supposed to be. Then outside both classes
I created a solve systems function that uses the addRows method that I created in the matrices class since this function
has a matrix parameter. It checks for division by zero every time we divide by a different number. Each addRows function
gets a zero in the 3x3 matrix except for the diagonal. Then for each row it divides the y value by the remaining value
in the diagonal to get the a, b, c values. I rounded them to two decimal places so then it can get to exactly what the
a, b, c values were and not need a function to check if it is close enough to the actual values. The function
makeSecretAndGiveOutShares makes random a, b, c values. I divided by 10 to get the possibilities of decimals and then
I rounded to two decimal places to match what I get when I solve for a, b, c. Then in a for loop of three times, I got
a random x value and did the same thing with the randint as I did for a, b, c. Then I made the row vectors, x^2, x, and 1
to be the coefficients for a, b, c that we are solving for. Then I plugged in the random x value to the equation
ax^2+bx+c with the known a, b, c to get the y-values and placed those into a column vector that will be added. These (x,y)
coordinates are random three coordinates that represent the zero-knowledge sharing protocol. Then I added the y-vector
to the 3x3 matrix of x values and used the solveEquations functions to get the a, b, c. Then I set secret equal to the c
value I got. I also printed the original a, b, c to show the user that the secret (c-value) is correct.