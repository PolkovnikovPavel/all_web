import sys
from io import BytesIO

import requests
from PIL import Image


def get_with_height_object(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    upper = toponym['boundedBy']['Envelope']['upperCorner'].split()
    point = toponym['Point']['pos'].split()

    w = abs(float(upper[0]) - float(point[0]))
    h = abs(float(upper[1]) - float(point[1]))
    return w, h


def get_params_for_static_maps(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    w, h = get_with_height_object(json_response)
    point = toponym['Point']['pos']

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(w), str(h)]),
        "l": "map",
        'pt': ','.join(point.split())}

    return map_params


toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

json_response = response.json()

map_params = get_params_for_static_maps(json_response)
map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
