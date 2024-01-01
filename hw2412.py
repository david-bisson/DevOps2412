# Create variables
#A

first = 7
second = 44.3

# Print result of adding first to second
print("Result of adding first to second:", first + second)

# Print result of multiplying first by second
print("Result of multiplying first by second:", first * second)

# Print result of dividing second by first
print("Result of dividing second by first:", second / first)

############################################################################
#B
a = 8
a = 17
a = 9
b = 6
c = a + b  # 15
b = c + a  # 24
b = 8  # 8
print("Value of a :", a)
print("Value of b :", b)
print("Value of c :", c)
##########################################################################
#C
Is there a difference between the two lines below? Why?
name = “john”
name = ‘john’
In terms of functionality and what they represent (as a string), there's no difference between single quotes and double quotes in Python. It's mostly a matter of personal preference or adhering to a particular style guide within a project. Some developers prefer using single quotes for simple string literals, while others may prefer double quotes. Python's standard style guide, PEP 8, doesn't prescribe one over the other; it's more about consistency within a codebase.

############################
What is the issue with the code below?
my_number = 5+5
print ("result is: " + my_number)
The issue with the code is a type mismatch error when concatenating a string with an integer.

In Python, you cannot directly concatenate a string with a non-string data type (like an integer) using the + operator without converting the non-string types to strings explicitly.

Here's the corrected version of the code:

answer: my_number = 5 + 5
print(f"result is: {my_number}")  # Using an f-string to format the output

########################################
#D
what will be the output
x=5
y= 2.36
print (x+int(y))
int(y) converts the floating-point value 2.36 to an integer, which becomes 2 (the decimal part is truncated).
Therefore, the expression x + int(y) evaluates to 5 + 2, which equals 7.

############################################
# CHALLENGE:
a = 8
B = "123"
print(a + int(B))

