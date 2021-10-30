#   Author:
#   Date:
#
#   Functions

#  example
#  processing
def calculate_discount_price(original_price, discount_percent):
    discount_amount = original_price * discount_percent / 100
    discounted_price = original_price - discount_amount
    return discounted_price


# input
my_original_price = float(input("Please enter original price: "))
my_discount_percent = float(input("Please enter discount percent: "))

# output
print("Discounted price =", calculate_discount_price(my_original_price, my_discount_percent))
print()


# task
# processing
def is_secret_word(word):
    secret_word = "secret"
    return word == secret_word


# input
my_secret_word = input("Please enter the secret word: ")
# output
print(is_secret_word(my_secret_word))
