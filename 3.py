# Example of if, elif, else statements

# Taking user input
num = int(input("Enter a number: "))

# Checking conditions and performing actions accordingly
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")

my_other_list = ["or","tohar","adam"]
my_other_name = "moshe"

if my_other_name in my_other_list:
    print(f"{my_other_name} is in the list.")
else:
    print(f"{my_other_name} is not in the list.")