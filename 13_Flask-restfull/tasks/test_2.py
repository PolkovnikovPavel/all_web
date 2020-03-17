from requests import get, post, delete, put

print(delete('http://127.0.0.1:8080/api/v2/users/5').json())
