# for i in range(5):
#     print("Hello " + str(i))
#
# for i in range(10):
#     print("your are number " + str(i))


def my_printer(prefix, amount_of_times):
    for i in range(amount_of_times):
        print(prefix + str(i))


def mul_five(my_number):
    result = my_number * 5
    return result


my_printer("Hello ", 5)
my_printer("you are number ", 10)

the_result = mul_five(50)
print(the_result)
