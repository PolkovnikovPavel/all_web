from requests import get, post, delete, put

print('\n2)посмотрим все данные первой работы')
print(get('http://127.0.0.1:8080/api/v2/jobs/1').json())