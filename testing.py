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

