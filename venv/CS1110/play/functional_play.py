print("\nPlaying with functions...\n")

'''def get_int_from_keyboard():
    print("Please enter an integer: ")
    str_input = input()
    if str_input.isdigit():     # minus signs are not digits
        return int(str_input)   # is a non-negative integer
    elif len(str_input)>1:      # check to see if it's a negative integer
        firstChar = str_input[0]
        minusPlus = False       # a default value which might change
        if firstChar == '+' or firstChar == '-':
            minusPlus = True
        if minusPlus and str_input[1: ].isdigit():
            return int(str_input)   # so it is a negative integer
    else:   # it'e neither a positive nor a negative integer
        print("OUCH -- you didn't give me what I wanted!!")
        return -999'''

def diagnostic(test=0,content="diagnostic help"):   # if i don't specify those values, these are the default values
    if test ==1:
        print(content)

# makes sure it only works with integers

'''def get_int_from_keyboard():
    print("Please enter an integer: ")
    str_input = input()
    print("you gave me " + str_input)   # diagnostic
    if str_input.isdigit():     # minus signs are not digits
        print("it's a non-negative integer")
        return int(str_input)   # is a non-negative integer
    
    # we only get here if we haven't already returned
    
    if len(str_input)>1:      # check to see if it's a negative integer
        firstChar = str_input[0]
        minusPlus = False       # a default value which might change
        if firstChar == '+' or firstChar == '-':
            minusPlus = True
        print("it's not a +ve int, but it's longish and minusPlus = " + str(minusPlus))
        if minusPlus and str_input[1: ].isdigit():
            print("it's a pos or neg integer... " + str_input)
            return int(str_input)   # so it is a negative integer
        print("it's longish but isn't digity after the first character")
    # it's neither a positive nor a negative integer
    print("OUCH -- you didn't give me what I wanted!!")
    return -999'''


def get_int_from_keyboard(show):
    print("Please enter an integer: ")
    str_input = input()
    diagnostic(show, "you gave me " + str_input)  # diagnostic
    if str_input.isdigit():  # minus signs are not digits
        diagnostic(show, "it's a non-negative integer")
        return int(str_input)  # is a non-negative integer

    # we only get here if we haven't already returned

    if len(str_input) > 1:  # check to see if it's a negative integer
        firstChar = str_input[0]
        minusPlus = False  # a default value which might change
        if firstChar == '+' or firstChar == '-':
            minusPlus = True
        diagnostic(show, "it's not a +ve int, but it's longish and minusPlus = " + str(minusPlus))
        if minusPlus and str_input[1:].isdigit():
            print("it's a pos or neg integer... " + str_input)
            return int(str_input)  # so it is a negative integer
        diagnostic(show, "it's longish but isn't digity after the first character")
    # it's neither a positive nor a negative integer
    print("OUCH -- you didn't give me what I wanted!!")
    return -999

print("\tabout to demonstrate how default values for functions work...\n")
diagnostic(0,"IO")
diagnostic(1)
diagnostic("this is a bit silly")       # thinks this is for the first variable (test value) not the content value even though we put in a string
diagnostic(1,"goofy")

show = 0    # doesn't print the diagnostic statements
# doubleMe = get_int_from_keyboard() * 2
compoundMe = get_int_from_keyboard() * get_int_from_keyboard()         # each time calls a new integer

print("\nTesting the function... \n" + str(compoundMe))
