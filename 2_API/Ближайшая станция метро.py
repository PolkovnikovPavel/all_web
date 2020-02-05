import requests


def find_metro(address):
    geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}$kind=metro&format=json"
    response = requests.get(geocoder_request)

    json_response = response.json()
    pos = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]['Point']['pos']

    geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={','.join(pos.split())}&kind=metro&format=json"
    json_response = requests.get(geocoder_request).json()

    metros = json_response['response']['GeoObjectCollection']['featureMember']
    if len(metros) == 0:
        return 'По близости нет метро'

    return metros[0]['GeoObject']['name']


print(find_metro(input()))

