# Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid number. Try again")

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.

# Use a try block to catch any arithmetic errors that may occur during the calculation.

# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

EXAMPLE_RECIPE = {
    "tablespoon olive oil": 1,
    "slices thick-cut bacon": 3,
    "cup (1-inch-diced) unpeeled Yukon Gold potatoes": 1,
    "extra-large eggs": 5,
    "tablespoons milk": 3,
    "tablespoon unsalted butter": 1,
    "tablespoon fresh chopped chives": 1
}


def conversion(original, desired): 
    try:
        ratio =  desired/original
    except OverflowError:
        print("Error: ",OverflowError)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Original Recipe:")
        for item, quantity in EXAMPLE_RECIPE.items():
            print(f"{quantity} {item}")
        print("New recipe with adjusted values: ")
        for item, quantity in EXAMPLE_RECIPE.items():
            new_quantity = ratio * quantity
            print(f"{new_quantity} {item}")
    finally:
        print("Enjoy cooking!")


original = get_number("Please enter your original serving size: ")
desired = get_number("Please enter your desized serving size: ")
conversion(original, desired)

