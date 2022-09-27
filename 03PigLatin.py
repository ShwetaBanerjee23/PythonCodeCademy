"""This is a Pig Latin translator. Pig Latin is a language game where the first letter
of a word is moved to the end and 'ay' is added to the end. So for instance, 'Python'
would become 'ythonpay'."""

print("Welcome to the Pig Latin Translator!\n\n")


def main_program():
    """ This function contains the code for the program. The code is written as
    a function to allow the code to be run several times depending on how many word
    the user wants to translate. """

    valid = False
    # ask user to input a word in English until word entered is valid
    while not valid:
        original = input("Please enter a word: ")
        if len(original) > 0 and original.isalpha():
            valid = True
        elif len(original) > 0 and not original.isalpha():
            print("\nInvalid input. Please enter letters only.\n")
        else:
            print("\nInvalid input. Please make sure you entered something.\n")

    # convert and display translated word
    translated = original[1:len(original)] + original[0] + "ay"

    print("The translated word for " + original.lower() + " is: " + translated)

    # check if user wants to translate another word
    flag = False
    # repeat until a valid input is entered
    while not flag:
        answer = input("\nWould you like to translate another word? ")
        if answer.lower() == "y" or answer.lower() == "yes":
            flag = True
            main_program()
        elif answer.lower() =='n' or answer.lower() == "no":
            flag = True
            print("\n\nThanks for using this Pig Latin Translator!")
        else:
            print("\nInvalid input. Please enter yes or no.\n")

main_program()
