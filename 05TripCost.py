# language used: Python 2

def hotel_cost(nights):
  """ This function calculates the cost of staying in a hotel depending on the number of nights spent at the hotel """
  
  return 140 * nights


def plane_ride_cost(city):
  """ This function calculates the cost of flying to four different cities in a plane """
  
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475


def rental_car_cost(days):
  """ This function calculates the cost of renting a car. The cost is $40 per day without discount. The discount given when renting a car is such that, when renting a car for over 7 days $50 is taken off the total cost and when renting a car for over 3 days, $20 is taken off the total. However, customers cannot have both discounts. """
  
  cost = 40 * days

  if days >= 7:
    cost -= 50
  # if statement runs first so customer renting a car for over 7 days does not get both discounts
  elif days >= 3:
    cost -= 20
  
  return cost

def trip_cost(city, days, spending_money):
  """ This function returns the total cost of the entire trip depending on which city the person is travelling to, the number of days they are travelling for and any extra money they spend on their vacation """

  # hotel_cost takes parameter nights which is equivalent to days - 1
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

# example vacation
print trip_cost("Los Angeles", 5, 600)
