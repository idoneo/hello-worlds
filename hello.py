#THis program says hello and asks name

print ('hello world')
#print is the function, what is in theparenthesis is what you are calling
print ('What is your name?')
myName = input()
# input function calls what is in the (), whatever is aded to
#input becoames a variable called myName
print ('Nice to meet you, ' + myName)
print ('The length of your name is:')
print (len(myName))
print ('How old are you?')
myAge = input()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')
#str(26) will convert the number 26 into a string
#int('26') will convert the word 26 into a number
str(26)
int('25')
#NOTE the input function always returns a STRING value even if the input is 26
# str(int(myAge) + 1) means convert myAge to an int, add 1 to it then turn it into
# a str so I can concatenate it to another string


