import requests
import random


def generate_random_names(num_names):
    random_names = []
    for _ in range(num_names):
        random_names.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(3, 8))))
    return random_names


def check_age(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url, verify=False)  # Disable SSL verification

    if response.status_code != 200:
        print(f"Failed to fetch age for name {name}.")
        return False

    age_data = response.json()
    age = age_data.get('age')
    if age is not None and 0 <= age <= 120:
        print(f"Age for {name} is {age}.")
        return True
    else:
        print(f"Age for {name} is invalid: {age}.")
        return False


if __name__ == "__main__":
    num_names = 3
    random_names = generate_random_names(num_names)
    for name in random_names:
        if check_age(name):
            print(f"Age for {name} is valid.")
        else:
            print(f"Age for {name} is invalid.")
