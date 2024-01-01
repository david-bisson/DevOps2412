def has_seven_or_divisible_by_seven(num):
    return num % 7 == 0 or '7' in str(num)

# Generating numbers from 1 to 100 and excluding numbers divisible by 7 or containing the digit 7
for i in range(1, 101):
    if not has_seven_or_divisible_by_seven(i):
        print(i, end=" ")