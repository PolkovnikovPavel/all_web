from io import BytesIO
from distance import lonlat_distance

import requests
from PIL import Image


def get_params_for_static_maps_and_organization(json_response, start_point):
    organizations = json_response["features"]
    grin_point = []
    blue_point = []
    grey_point = []

    for i in range(10):
        organization = organizations[i]
        point = organization["geometry"]["coordinates"]
        org_point = "{0},{1}".format(point[0], point[1])

        Availabilities = organization['properties']['CompanyMetaData'][
            'Hours']['Availabilities'][0]

        if 'TwentyFourHours' in Availabilities:
            grin_point.append(org_point)
        elif 'TwentyFourHours' not in Availabilities:
            blue_point.append(org_point)
        else:
            grey_point.append(org_point)

    grin_text = ",pm2gnm~".join(grin_point)
    if len(grin_point) > 0:
        grin_text += ',pm2gnm'
    if len(blue_point) > 0 and len(grin_point) > 0:
        grin_text += '~'

    blue_text = ",pm2blm~".join(blue_point)
    if len(blue_point) > 0:
        blue_text += ',pm2blm'
    if len(grey_point) > 0 and len(blue_point) > 0:
        blue_text += '~'

    grey_text = ",pm2grm~".join(grey_point)
    if len(grey_point) > 0:
        grey_text += ',pm2grm'

    map_params = {
        "l": "map",
        'pt': f'{grin_text}{blue_text}{grey_text}'}

    return map_params


def get_data_of_organization(organization):
    text = []
    start_point = list(map(float, address_ll.split(',')))
    org_point = organization['geometry']['coordinates']

    name = organization['properties']['name']
    address = organization['properties']['description']
    time_of_work = organization['properties']['CompanyMetaData']['Hours']['text']

    distance = int(lonlat_distance(start_point, org_point))

    text.append(f'Название: {name}')
    text.append(f'Адрес: {address}')
    text.append(f'Время работы: {time_of_work}')
    text.append(f'Растояние: {distance}')
    return '\n'.join(text)


# toponym_to_find = " ".join(sys.argv[1:])
toponym_to_find = 'Кемерово Радищева 6'

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
    "type": "biz",
    "results": 50
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()
map_params = get_params_for_static_maps_and_organization(
                                                    json_response, address_ll)

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
