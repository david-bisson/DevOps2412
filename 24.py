import requests

## response = requests.delete("http://localhost:8080/items/1")
response = requests.get("http://localhost:8080/items")
actual = len(response.json())
print ("actual ", actual)
expected = 3
print ("expected ", expected)
assert expected == actual
