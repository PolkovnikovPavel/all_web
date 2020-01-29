import os
import sys

import pygame
import requests

response = None
map_request = "https://yandex.ru/maps/2/saint-petersburg/?from=api-maps&ll=30.128674%2C59.918158&mode=usermaps&origin=jsapi_2_1_75&um=constructor%3ApWM9zklGJOzTDlcUjCLZZ2_i7lBnvyDO&z=11.57"

response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)