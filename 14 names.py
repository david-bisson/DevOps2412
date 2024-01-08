def add_names_to_file():
    # Ask for 3 names from the user
    names = []
    for i in range(3):
        name = input(f"Enter name {i + 1}: ")
        names.append(name)

    # Append the names to the names.txt file
    with open("names.txt", "a") as file:
        for name in names:
            file.write(name + "\n")


def print_hello_and_names():
    # Read names from the names.txt file and print "Hello" with each name
    with open("names.txt", "r") as file:
        names = file.readlines()
        for name in names:
            print(f"Hello {name.strip()}")


# Add names to the file
add_names_to_file()

# Print "Hello" and all the names from the file
print_hello_and_names()
