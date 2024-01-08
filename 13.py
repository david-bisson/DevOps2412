my_file = open("names.txt")
for name in my_file.readlines():
    print(f"hello {name}")
    