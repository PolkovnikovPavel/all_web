import requests

address = input()
port = input()
a = input()
b = input()

url = f'{address}:{port}'

params = {
    "a": a,
    "b": b}

response = requests.get(url, params=params)
json_response = response.json()


result = json_response['result']
key = json_response['check']

result.sort()

print(result[0], result[1])
print(key)
