import requests


# Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
# and make sure that israel has at least 5 universities
def get_universities(country_code):
    url = f"http://universities.hipolabs.com/search?country={country_code}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data for country {country_code}.")
        return None

    universities = response.json()
    return universities


if __name__ == "__main__":
    country_code = "Israel"
    universities = get_universities(country_code)
    if universities:
        print(f"List of universities in {country_code}:")
        for university in universities:
            print(f"- {university['name']}")
    else:
        print("No universities found.")
