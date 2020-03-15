from requests import get, post, put

print('1)')
print(get('http://127.0.0.1:8080/api/jobs').json())
# 1)смотрим все работы до добавления

print('\n2)')
print(post('http://127.0.0.1:8080/api/jobs',
           json={'job': 'Ещё одно задание',
                 'team_leader': '4',
                 'work_size': '28',
                 'collaborators': '2, 3, 4',
                 'is_finished': False,
                 'id': '12'}).json())
# 2)добовляем новую работу с id = 12

print('\n3)')
print(get('http://127.0.0.1:8080/api/jobs').json())
# 3)смотрим все работы после добавления

print('\n4)')
print(put('http://127.0.0.1:8080/api/jobs/12',
           json={'job': 'Ещё одно задание(изменённое)',
                 'team_leader': '4',
                 'work_size': '48',
                 'collaborators': '3, 4',
                 'is_finished': True}).json())
# 4)изменим работу с id = 12

print('\n5)')
print(get('http://127.0.0.1:8080/api/jobs/12').json())
# 5)убедимся, что изменения пременились

print('\n6)')
print(put('http://127.0.0.1:8080/api/jobs/12',
           json={'job': 'Ещё одно задание(дважды измен.)',
                 'team_leader': '4455452',
                 'work_size': '48',
                 'collaborators': '3, 4',
                 'is_finished': True}).json())
# 6)попытаемся изменить team_leader(несуществующий) и название

print('\n7)')
print(get('http://127.0.0.1:8080/api/jobs/12').json())
# 7)убедимся, что изменения НЕ пременились


print('\n8)')
print(put('http://127.0.0.1:8080/api/jobs/12',
           json={'job': 'Ещё одно задание(дважды измен.)',
                 'team_leader': '4455452',
                 'collaborators': '3, 4',
                 'is_finished': True}).json())
# 8)попытаемся изменить работу не передав work_size

print('\n9)')
print(get('http://127.0.0.1:8080/api/jobs/12').json())
# 9)убедимся, что изменения НЕ пременились
