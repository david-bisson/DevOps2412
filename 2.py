x = 2
if x == 2:
    print("x is 2")

# my_name = input("enter your name: ")
# if my_name == "aviel":
#     print("good!")

a = 4
b = 14
if a < b:
    print("a is lower")

result = 14 % 3
print(result)

fname = "dudi"
lname = "bisson"
full_name = "David " + "Bisson"
another_full_name = "%s %s" % (fname, lname)
another_full_name2 = f"{fname} {lname}"
another_full_name3 = "{} {}".format(fname, lname)
another_full_name4 = 'name: "dudi"\nmarried: yes\nage: 34'
print(another_full_name)
print(another_full_name2)
print(another_full_name3)
print(another_full_name4)
