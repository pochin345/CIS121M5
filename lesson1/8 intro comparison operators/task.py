#   Author:
#   Date:
#
#   Comparisons
#
#   no coding necessary
#   just run the tests

# input
number1_string = input("Please enter an integer: ")
number2_string = input("Please enter another integer: ")
upperB = "B"
lowerB = "b"

# processing
number1_integer = int(number1_string)
number2_integer = int(number2_string)

#output
print()
print("As strings,", '"' + number1_string + '"', ">",
      '"' + number2_string + '"', "is",
      number1_string > number2_string)

print("As integers,", number1_integer, ">",
      number2_integer, "is", number1_integer > number2_integer )
print()

print('The ASCII value of "' +  upperB + '" is', ord(upperB))
print('The ASCII value of "' + lowerB + '" is', ord(lowerB))
print(' so "' + lowerB + '" > "' + upperB + '" is', lowerB > upperB)
