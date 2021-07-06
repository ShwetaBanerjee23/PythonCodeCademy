"""
This program uses basic arithmetic to calculate the total cost a customer needs to pay at a hotel
"""

# add your meal cost here
mealCost = 44.5
# add restaurant tax here after converting from percentage to decimal
restaurantTax = 0.0675
# add tip here after converting from percentage to decimal
tip = 0.15

# this calculates the total amount you have to pay
mealCost += restaurantTax * mealCost + tip * (mealCost + restaurantTax * mealCost)

print(mealCost)
