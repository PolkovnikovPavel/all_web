import os
import sys

import pygame
import requests

response = None

pls = ['29.914692%2C59.891711', '30.211905%2C59.967651',
       '30.310309%2C59.946159', '30.316965%2C59.942636']

map_request = f"http://static-maps.yandex.ru/1.x/?ll=30.045630%2C59.928810&spn=0.156,0.156&l=map&pl={','.join(pls)}"

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
