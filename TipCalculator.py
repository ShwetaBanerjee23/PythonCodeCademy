mealCost = 44.5
restaurantTax = 0.0675 * mealCost
tip = 0.15 * (mealCost + restaurantTax)

mealCost += restaurantTax + tip

print(mealCost)