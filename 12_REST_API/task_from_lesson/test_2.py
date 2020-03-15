from requests import get, post, delete, put

print(put('http://127.0.0.1:8080/api/jobs/6',
           json={'job': 'Ещё одно задание(уже второй раз)',
                 'team_leader': '4',
                 'work_size': '48',
                 'collaborators': '3, 4',
                 'is_finished': True}).json())
