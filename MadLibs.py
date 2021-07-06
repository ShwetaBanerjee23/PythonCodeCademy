"""
This program generates passages that are generated in mad-lib format. It prompts 
the user for inputs and then prints the story with the inputs matched to the 
right places. It uses basics of Python including user inputs, print statements 
and string concatenation and string formatting.

Author: Shweta Banerjee
"""

# The template for the story

STORY = """This morning {} woke up feeling {}. 'It is going to be a {} day!' 
Outside, a bunch of {}s were protesting to keep {} in stores. They began to 
{} to the rhythm of the {}, which made all the {}s very {}. Concerned, {} 
texted  {}, who flew {} to {} and dropped {} in a puddle of frozen {}. {} 
woke up in the year {}, in a world where {}s ruled the world."""

print("----------------------")
print("----------------------\n")
print("Mad Libs has started!\n")
print("----------------------")
print("----------------------\n\n")

# 1 name is needed for the story

name = input("Enter a name: ")

# 3 adjectives are needed for the story

print("Please enter 3 adjectives:")
adjective1 = input("Adjective 1: ")
adjective2 = input("Adjective 2: ")
adjective3 = input("Adjective 3: ")

# 1 verb is needed for the story

verb = input("Please enter a verb: ")

# 2 nouns are needed for the story

print("Please enter 2 nouns:")
noun1 = input("Noun 1: ")
noun2 = input("Noun 2: ")

# some other words are also needed for the story

print("Please enter one of each of the following - in singular form, where applicable:")
animal = input("Animal: ")
food = input("Food: ")
fruit = input("Fruit: ")
superhero = input("Superhero: ")
country = input("Country: ")
dessert = input("Dessert: ")
year = str(input("Year: "))

# adding words to the story in order

updatedStory = STORY.format(name, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3,
                            name, superhero, name, country, name, dessert, name, year, noun2)

# printing the story with user input

print(updatedStory)
