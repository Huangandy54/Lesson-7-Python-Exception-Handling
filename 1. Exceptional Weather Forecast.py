# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start
# Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

# Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.
def get_fahrenheit(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid number. Try again")

fahrenheit = get_fahrenheit("Please enter your temperature: ")


# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

def convert_to_celcius(fahrenheit):
    try:
        result=  (fahrenheit - 32) * 5/9
    except OverflowError:
        print("Error: ",OverflowError)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"{fahrenheit} Fahrenheit is equal to {result} Celcius")
    finally:
        print("Thanks for using the weather forecast application!")

convert_to_celcius(fahrenheit)
# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.

# Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.