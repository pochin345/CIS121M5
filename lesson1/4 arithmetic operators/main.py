#   Author:
#   Date:
#
#   Calculate discount price

original_price = float(input("Please enter original price: "))
discount_percent = float(input("Please enter discount percent: "))

discount_amount = original_price multiply discount_percent divide 100
discounted_price = original_price subtract discount_amount

print("Discounted price =", discounted_price)
