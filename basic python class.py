print("Hello World")
spam = 42
spam 
###################################### How to Find Help #################################
# Solving programming problems on your own is easier
# than you might think. If you're not convinced, then
# let's cause an error on 
# purpose: Enter '42' + 3 into the interactive shell.
# You don't need to know what this instruction means
# right now, but
# the result should look like this:
'42'+3
# The second error message (i.e., can only ...) appeared here because
# python couldn't understnd your instruction and line number that python had trouble with. If you are not sure what to make of a particular error message, search online for the 
# exact error message.
#################################### Entering Expressions in python ###########
# Expressions consists of values and operators that reduce down to a single value (including combinations of numbers and strings).
2 + 2
2 + 3 * 6
(2 + 3) * 6
2 * 8
2 ** 8 #(this is exponentiaol maths )
23/7 #division
23 // 7 #interger division /floored quotient
23 % 7 # Modulo/remainder
(5-1)*(7+1)/(3-1) 
56%5
# The rules for putting operators and values together to form expresiions are a fundamental part of python as a proggramming language, just like the grammar rules that hlp us communicate
# example: 
# -------------This is a grammatically correct English sentence
#------------- This grammatically is sentence not english correct a
# The second line is difficult to parse because it doesnt the rules of English. Similarly, if you type in a bad python instruction, python wont be able to understand
# it and will display a syntaxError error message, as shown here:
5 + 
42 + 5 + * 2
####################### The integer, Floating point and string Data.Remeber that expressions are just values combined with operators, and they always evaluate down to a single
## value. A data type is a category for values, and every value belong to exactly one data type. The most common data types in python are:
 # 1. Integers : -2, -1, 0, 1, 2 etc
 # 2. Floating numbers : -1.25, -1.0, 0.5
 # 3. strings: 'a', 'Hello!', 'Goodbye cruel world!'
 'Hello World!'
 'Hello World!
 # If you ever see the error message "SyntaxError: EOL while scanning string literal", you probably forgot the final single quote character at the end of the string, such as in the example above.
 ######################## String Concatenation and Replication ##################
 'Alice' + 'Bob'
 'Alice' * 5 # The expression evaluates down to a single string value that repeats the original a number of equal times equal to the integer value.
 'Alice' * 'Bobo' # The operator can be used with only two numeric values (for multiplication) or one string value and one integer value (for string replication).
 # otherwise python will just display an error message
  'Alice' * 5.0
  'Hello' + '!' * 10
  ###################################### Storing Values in Variables##################
   # A Variable is like a box in the computer's memory where you can store a single value. If you want to use the result of an evaluated expression
   # later in your program, you can save it inside a variable.
   # Assignment Statements: You will store values in variables with an assignment statement. An asignment statement consists of a variable name, 
   # and the value to be stored. If you enter the assignment statement spam = 42, then a variable named 'spam' will have the integer value 
   # 42 stored in it.
   spam = 40
   spam
   eggs = 2
   spam + eggs
   spam = spam + 2
    spam
    spam = 'Hello' # This is called overwriting the variable
    spam
    spam = 'Goodbye'
    spam
    spam + 'World'
    ############################# Your First Program ###################
    # This program says hello and asks for your name:
    print('What is your name?')# print() function displays the string value inside the parenthesis on the screen
    myName = input() # print() function waits for the user to type some text on the 
    print('Nice to meet you,' + myName)
    print('The length of your is:')
    print(len(myName)) 
    print('What is your age?')
    myAge = input()
    print('You will be' + str(int(myAge) + 1) + 'in a year.')
    ## NOTE: The program will wait until the input is entered before continuing to execute the remaining code
    ################### The str(), int(), and float() functions #####################
    # If you want to concatenate an integer such as 29 with a string to pass to print(), you will need to get the value '29',
    # which is the string form of 29. The str() function can be passedan integer value and will evaluate to a string value version of it, as fololows:
    str(0)
    str(-3.14)
    int('42')
    int(1.25)
    int(7.7) + 1
    float('3.14')
    float(10)

print("mes")









