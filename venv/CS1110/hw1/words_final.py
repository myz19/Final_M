no_of_lines = int(input("Enter the number of lines of text: "))     # asks the user to input the number of lines of text they want
lines = ""      # initializes a new variable to the empty string
print("Enter text: ")
for i in range(no_of_lines):    # uses a for loop to allow the user to input many lines of text since python doesn't allow that itself
   lines += input() + " "
print(lines)

word_list = lines.replace(".", " ").replace(","," ").replace("!", " ").replace("?"," ").split()     # removes any punctuation and splits the string by spaces into a list

print(word_list)

unique_word_length = []     # initializes a new empty list
for word in word_list:      # for loop that adds to the new list every unique word length
    if len(word) not in unique_word_length:
        unique_word_length.append(len(word))

print(unique_word_length)

unique_word_length.sort()   # sorts the list in ascending order

for word_length in unique_word_length:      # use a for loop to create a new list for every unique word length
    x=[]
    for word in word_list:          # use a for loop to add words to each list of each word length if the length of the words of the text is the same as the unique lengths
        if len(word) == word_length:
            x.append(word)
    print(x)        # prints each list of unique word lengths
    print("There are ", len(x), " word(s) in this list of ", word_length, " letter words.")     # prints out a statement saying how many words are in each list of each word length

