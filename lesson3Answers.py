from PIL import Image

# 1. Write the following code: a = 1/0;
#
# 2. Build a corresponding try-except block to
# avoid exception.

try:
    a = 1 / 0
except ZeroDivisionError as e:
    print("Error:", e)
    # Handle the division by zero exception here
    # You can print a message, assign a default value to 'a', or perform any other desired action.
    a = 0  # Assigning a default value of 0 to 'a' in this case

# 3. Is the following code legal?
# try :
#  x = 1
# finally :
#  print(“finally”)
#
# The code you provided is almost correct, but the string within the print() statement appears to contain special characters that might not be recognized as regular quotes. If you're using Python, ensure that you use either single (') or double (") quotes for strings, but make sure they are consistent.
#
# Here's the corrected code:
try:
    x = 1
finally:
    print("finally")



# 4. What exception types can be caught by the
# following handler?
# Except:
# In Python, the except statement is used in a try-except block to catch exceptions.
# When you see except: without specifying a particular exception type, it acts as a catch-all for any type of exception that might occur within the associated
# try block.
# This means it will catch all exceptions, including built-in exceptions
# like TypeError, ValueError, ZeroDivisionError, as well as user-defined exceptions and system-exiting exceptions like SystemExit and KeyboardInterrupt.


# 5. What is wrong with using the above type of
# exception handler?

 # it's generally recommended to be more specific in exception handling whenever possible, '
 #    'to handle specific exceptions separately and avoid catching more exceptions than necessary. For instance
# try:
#     # Some code that might raise exceptions
#     pass
# except ExceptionType1:
#     # Handle ExceptionType1
#     pass
# except ExceptionType2:
#     # Handle ExceptionType2
#     pass
# except:
#     # Handle all other exceptions
#     pass

#
# 6. What exceptions can be caught by the
# following handlers?
# ...
# except IOError
# …IOError: This exception is raised when an input/output operation fails, such as attempting to open a file that doesn't exist or trying to read from a file without proper permissions.
#
# except ZeroDivisionError
# ZeroDivisionError: This exception is raised when attempting to divide a number by zero, which is mathematically undefined.

# 7. Create a text file named “words.txt”
# 8. Write your name into the file
# programmatically
file_name = "words.txt"

# Open the file in write mode ('w')
with open(file_name, 'w') as file:
    # You can write content to the file if needed
    # For example, writing some initial text to the file
    file.write("This is a text file named 'words.txt'.\n")
    # You can also leave it empty by not writing anything
    file.write("My Name is David Bisson.")

# 9. Read your file content and print it
with open(file_name, 'r') as file:
    file_content = file.read()
    print(file_content)

# 10. Write Hebrew content into your text file and
# print its content programmatically.
# Hebrew text to be written into the file
hebrew_text = "\u202eזהו קובץ טקסט בעברית.\u202c"

# Write Hebrew content to the file
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(hebrew_text)

# Read and print the file's content
with open(file_name, 'r', encoding='utf-8') as file:
    file_content = file.read()
    print(file_content)

# Challenge:
# 11. Create an image from code (png file) Hint:
# use Pillow

# Create a new blank image with mode 'RGB' (Red, Green, Blue)
width, height = 200, 200
color = (255, 0, 0)  # Red color represented in RGB format
image = Image.new("RGB", (width, height), color)

# Save the image as a PNG file
file_name = "red_square.png"
image.save(file_name)

# Display a confirmation message
print(f"Image '{file_name}' created successfully!")