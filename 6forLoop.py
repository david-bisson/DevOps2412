# for i in range(5):
# print("Hello " + str(i))

class_mates = ["dudi", "yoni", "gilad", "oren"]
for name in class_mates:
    if name == "yoni":
        name = "amir"
    print(name)

# index based
for i in range(len(class_mates)):
    print(class_mates[i])

your_name = input("ener your name: ")
while your_name != "aviel":
    print("you are not aviel")
    your_name = input("enter your name")
