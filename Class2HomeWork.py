# ********* A  ************

# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.

# Step 1: Create two variables X and Y
X = 10
Y = 5

# Step 2: Print "BIG" if X is bigger than Y
if X > Y:
    print("BIG")

# Step 3: Print "small" if X is smaller than Y
if X < Y:
    print("small")

# ********* B  ************
# 1. Run a “for” loop 5 times.
# 2. Print iteration number every time.
# Using a for loop to iterate 5 times
for i in range(1, 6):  # Range from 1 to 5 (inclusive)
    # Printing the iteration number
    print("Iteration number:", i)

# ********* C  ************
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
#
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
# Create a variable and initialize it with a number 1-4

season_number = 3  # You can change this number to test different scenarios

# Check the variable and print the corresponding season name
if season_number == 1:
    print("Summer")
elif season_number == 2:
    print("Winter")
elif season_number == 3:
    print("Fall")
elif season_number == 4:
    print("Spring")
else:
    print("Invalid season number")  # Handling cases where the number is not in the range 1-4

# ********* D  ************
# 1. how many times will the following loop run? Answer - 10
# 2. what will be printed last? Answer - 10
count = 1
while count < 11:
    print(count)
    count = count + 1

# ********* E  ************
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
#
# ● Print all variables.
# ● Add the currency to your age, and check the result.

# Variables holding the information
age = 43  # Replace with your actual age
last_name_first_letter = 'B'  # Replace with the first letter of your last name
shekels_to_dollar_currency = 3.6  # Replace with the current shekels-dollar currency
flew_abroad = True  # Replace with true or false based on whether you flew abroad
apartment_number = 15  # Replace with your apartment number

# Printing all variables
print("Age:", age)
print("First letter of last name:", last_name_first_letter)
print("Shekels-Dollar currency:", shekels_to_dollar_currency)
print("Flew abroad:", flew_abroad)
print("Apartment number:", apartment_number)

# Adding currency to age and checking the result
result = age + shekels_to_dollar_currency

print("Age + Shekels-Dollar currency:", result)

# ********* F  ************
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the
# user entered.

# Ask the user for their phone number
phone_number = input("Please enter your phone number: ")

# Print the words "phone number" and the entered phone number
print("phone number:", phone_number)


# ********* G  ************
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the
# result.

# Method named printHello() that prints the word “hello”
def printHello():
    print("hello")


# Method named calculate() which adds 5+3.2 and prints the result
def calculate():
    result = 5 + 3.2
    print("The result of 5 + 3.2 is:", result)


# Calling the functions
printHello()
calculate()


# ********* H  ************
# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the
# result.

# Method that receives a name and prints it
def print_name(name):
    print("Your name is:", name)


# Method that receives a number, divides it by 2, and prints the result
def divide_by_2(number):
    result = number / 2
    print("The result of dividing", number, "by 2 is:", result)


# Example usage of the functions
# You can replace the arguments with your desired inputs

# Calling the print_name() function
user_name = input("Please enter your name: ")
print_name(user_name)

# Calling the divide_by_2() function
user_number = float(input("Please enter a number: "))  # Convert input to float for division
divide_by_2(user_number)


# ********* I  ************

# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the
# sum.
# 2. Method that receive two Strings, add space between them,
# and return one spaced string.

# Method that receives two numbers, adds them, and returns the sum
def add_numbers(num1, num2):
    return num1 + num2


# Method that receives two strings, adds space between them, and returns one spaced string
def add_strings(str1, str2):
    return f"{str1} {str2}"


# Example usage of the functions
# You can replace the arguments with your desired inputs

# Calling the add_numbers() function
result_sum = add_numbers(5, 7)
print("The sum of the two numbers is:", result_sum)

# Calling the add_strings() function
result_string = add_strings("Hello", "World")
print("The combined string with space is:", result_string)

#Challenges:
# ********* K  ************
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:
# Define the number of rows for the pyramid
rows = 5

# Nested for loop to create the pyramid shape
for i in range(rows):  # Outer loop for the number of rows
    for j in range(i + 1):  # Inner loop to print the asterisks in each row
        print("*", end="")
    print()  # Move to the next line after each row is printed


# ********* L  ************
# Create a nested for loop to create X shape (width is 7,
# length is 7):

# Define the size of the X shape
size = 7

# Nested for loop to create the X shape
for i in range(size):  # Loop through each row
    for j in range(size):  # Loop through each column
        if j == i or j == size - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to the next line after each row is printed

# ********* M  ************

# Write a program with the following:
# 1. Method that gets a number from the user (using input).
# 2. Method that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)

# Method that gets a number from the user using input
def get_number_from_user():
    user_input = input("Please enter a number: ")
    return int(user_input)  # Convert the input to an integer

# Method that computes the sum of the digits of an integer
def compute_sum_of_digits(number):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    return sum_of_digits

# Get a number from the user
user_number = get_number_from_user()

# Calculate and print the sum of its digits
sum_of_digits_result = compute_sum_of_digits(user_number)
print("The sum of digits in the number is:", sum_of_digits_result)

