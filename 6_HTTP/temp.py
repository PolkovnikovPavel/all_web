import requests


address = input()
port = input()
a = input()
b = input()

url = f'{address}:{port}?a={a}&b={b}'
response = requests.get(url)
json_response = response.json()

result = json_response['result']
key = json_response['check']

result.sort()

print(' '.join(result))
print(key)
