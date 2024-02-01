import requests
import random

# Testing Github API - Create a program in python that goes to the following API and
# checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos
def check_repositories_exist(username, min_repos=5):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch repositories for user {username}.")
        return False

    repos = response.json()

    if len(repos) >= min_repos:
        print(f"{username} has at least {min_repos} repositories.")
        return True
    else:
        print(f"{username} has less than {min_repos} repositories.")
        return False


if __name__ == "__main__":
    username = "avielb"
    min_repos = 5
    if check_repositories_exist(username, min_repos):
        print("Proceed with further actions...")
    else:
        print("Insufficient repositories. Action halted.")
