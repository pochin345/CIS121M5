#   Author:
#   Date:
#
#   imprecision of float
#
#   no coding necessary
#   just run the tests

# input
test_number = float(input("Please enter a number: "))

# process
multiply_by_itself = test_number * test_number

print("precision error (sometimes)",multiply_by_itself)
print("precise to 2 decimal places", round(multiply_by_itself,2))



