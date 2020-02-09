import os

import pygame
import requests


def create_slide(index):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords_text[index][0]}&l=sat&z={coords_text[index][1]}"
    response = requests.get(map_request)
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))

    font = pygame.font.Font(None, 19)
    text = font.render(map_request, 1, coords_text[index][3])
    screen.blit(text, (5, 411))

    font = pygame.font.Font(None, 27)
    text = font.render(coords_text[index][2], 1, coords_text[index][3])
    screen.blit(text, (5, 390))


pygame.init()
screen = pygame.display.set_mode((600, 450))
map_file = 'map.png'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
index = 0
running = True
coords_text = [('37.618631%2C55.755004', '17', 'Московский Исторический музей', WHITE),
               ('31.133709%2C29.979208', '17', 'Пирамида хеопса', BLACK),
               ('79.073987%2C59.416610', '3', 'Евразия', WHITE),
               ('2.294926%2C48.858179', '18', 'Эйфелева башня', WHITE),
               ('37.623014%2C55.752590', '19', 'Московский кремль', WHITE)]

create_slide(0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            index += 1
            if index == len(coords_text):
                index = 0
            create_slide(index)

    pygame.display.flip()

pygame.quit()
os.remove(map_file)
