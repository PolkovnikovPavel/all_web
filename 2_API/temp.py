import os

import pygame
import requests

ck = {'inUserName': 'Полковников', 'inUserPass': '123456'}

map_request = f"https://cabinet.ruobr.ru/child/studies/mark_table/?school_year=2019&period=3&csrfmiddlewaretoken=gYa4KG3hcmT8oZP9N2ZvViishtogCR4a&_xsrf=null"
response = requests.get(map_request, data=ck)
print(response.text)




