#   Author:
#   Date:
#
#   Logical Operators

# Just examples: no code necessary
# Just run the code

a = 12
b = 20

print("a = ", a)
print("b =", b)
print()

# a number can never be both greater than another number and also less than it
print("(a > b) and (b > a) is ",(a > b) and (b > a))
print("since a value can't simultaneously be greater than and less than another number")
print()

# as long as a number isn't equal to another number,
# it must be either greater than or less than the other number
print("(a > b) or (b > a) is ",((a > b) or (b > a)))
print("since unless they are equal, a value must be less or greater than another value")
print()

# not changes True to False and False to True
print("a < b is", a < b)
print ("not (a < b) is", not (a < b))
print()

print("a > b is", a > b)
print ("not (a > b) is", not (a > b))
print()

# Enter state and print True if state allows self serve gas
# Only OR and NJ don't allow self serve gas
state = input("Please enter state abbreviation: ")
print("Allows self serve gas?", not(state.upper() == "OR" or state.upper() == "NJ"))


