import requests

sites = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']


for sity in sites:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={sity}&format=json"
    response = requests.get(geocoder_request)

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    subject = toponym['metaDataProperty']['GeocoderMetaData']['Address'][
        'Components'][2]['name']

    print(f'{sity} - {subject}')
