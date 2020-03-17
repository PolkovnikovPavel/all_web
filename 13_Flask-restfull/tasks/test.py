from requests import get, post, put, delete

print('1)')
print(get('http://127.0.0.1:8080/api/v2/users').json())
# 1)смотрим всех пользователей

print('\n2)')
print(get('http://127.0.0.1:8080/api/v2/users/1').json())
# 2)посмотрим все данные капитана

print('\n3)')
print(post('http://127.0.0.1:8080/api/v2/users',
           json={'surname': 'Nosurname',
                 'name': 'Noname',
                 'age': 56,
                 'position': 'navigator',
                 'speciality': 'research engineer',
                 'address': 'module_4',
                 'email': 'noname_nosurname@mars.org',
                 'hashed_password': '1234567890abc'}).json())
# 3)добавим нового пользователя


print('\n4)')
users = get('http://127.0.0.1:8080/api/v2/users').json()
print(users)
# 4)убедимся, что новый пользователь добавлен


print('\n5)')
id = users['users'][-1]['id']
print(put(f'http://127.0.0.1:8080/api/v2/users/{id}',
           json={'surname': 'Nosurname',
                 'name': 'Noname',
                 'age': 26,
                 'position': 'navigator',
                 'speciality': 'research engineer',
                 'address': 'module_4',
                 'email': 'noname_nosurname@mars.org',
                 'hashed_password': '1234567890abc'}).json())
# 5)изменим возрост новому пользователю


print('\n6)')
print(get(f'http://127.0.0.1:8080/api/v2/users/{id}').json())
# 6)убедимся, что изменение прошло успешно


print('\n7)')
id = users['users'][-1]['id']
print(put(f'http://127.0.0.1:8080/api/v2/users/{id}',
           json={'surname': 'Nosurname',
                 'name': 'Noname',
                 'age': 'двадцать семь',
                 'position': 'navigator',
                 'speciality': 'research engineer',
                 'address': 'module_4',
                 'email': 'noname_nosurname@mars.org',
                 'hashed_password': '1234567890abc'}).json())
# 7)попробуем опять сменить возрост, но передадим его в виде строки


print('\n8)')
print(get(f'http://127.0.0.1:8080/api/v2/users/{id}').json())
# 8)убедимся, что изменение не получилось


print('\n9)')
print(delete('http://127.0.0.1:8080/api/v2/users/995952962985999').json())
# 9)попытаемся удалить несуществующего пользователя

# далее проверять коректность не будем т.к. из сообщения понятно: удалось или нет


print('\n10)')
print(delete(f'http://127.0.0.1:8080/api/v2/users/{id}').json())
# 10)удалим создоного пользователя


print('\n11)')
print(get(f'http://127.0.0.1:8080/api/v2/users/{id}').json())
# 11)попытаемся посмотреть данные удалённого пользователя


print('\n12)')
print(post('http://127.0.0.1:8080/api/v2/users',
           json={'surname': 'Nosurname',
                 'age': 56,
                 'position': 'navigator',
                 'speciality': 'research engineer',
                 'address': 'module_4',
                 'email': 'noname_nosurname@mars.org',
                 'hashed_password': '1234567890abc'}).json())
# 12)попытаемся добавить нового пользователя, но забудем передать name
