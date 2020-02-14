import sys
from io import BytesIO

import requests
from PIL import Image


def get_params_for_static_maps_and_organization(json_response, start_point):
    organization = json_response["features"][0]
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])

    map_params = {
        "l": "map",
        'pt': f'{start_point},pm2al~{org_point},pm2bl'}

    return map_params, organization


def get_data_of_organization(organization):
    text = []
    start_point = list(map(float, address_ll.split(',')))
    org_point = organization['geometry']['coordinates']

    name = organization['properties']['name']
    address = organization['properties']['description']
    time_of_work = organization['properties']['CompanyMetaData']['Hours']['text']
    distance = int(((abs(start_point[0] - org_point[0]) ** 2 + abs(
        start_point[1] - org_point[1]) ** 2) ** 0.5) * 68388)

    text.append(f'Название: {name}')
    text.append(f'Адрес: {address}')
    text.append(f'Время работы: {time_of_work}')
    text.append(f'Растояние: {distance}')
    return '\n'.join(text)


toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass

json_response = response.json()
address_ll = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]['Point']['pos']
address_ll = ','.join(address_ll.split())

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()
map_params, organization = get_params_for_static_maps_and_organization(
                                                    json_response, address_ll)

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)


print(get_data_of_organization(organization))

Image.open(BytesIO(response.content)).show()
