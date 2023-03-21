
# a shop wishes to give a discount of discount % tot he most expensive item purchased 
# by a given customer during sales period. Only one product can benefit from the discount. 
# you are tasked with implmenting a func of calulcate_total(prices, discount) which takes
# the list of prices of the products purchased by a customer and the 
# percentage discount as paramters and returns the total purchase price as an integer(rounded down) 
# if the total is a float number


import math

def calculate_total(prices, discount):
    max_price = max(price)
    discount_amount = math.floor(max_price * (discount / 100))
    purchase_price = sum(prices) - discount_amount
    if isinstance(purchase_price, float):
        return math.floor(purchase_price)
    else:
        return purchase_price
      
      
 prices = [10, 20, 30, 40, 50]
discount = 20
total = calculate_total(prices, discount)
print("The total purchase price is:", total)
