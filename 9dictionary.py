my_class = [
    {"fname": "or", "lname": "shemesh"},
    {"fname": "maksim", "lname": "hamaksim"},
]

# Iterate through each dictionary in my_class
for student in my_class:
    # Print the key-value pairs for each dictionary
    print("Student:")
    for key, value in student.items():
        print(f"{key}: {value}")
    print()  # Print an empty line for better readability between students
