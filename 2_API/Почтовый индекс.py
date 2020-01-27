import requests

addresses = ['Петровки, 38']


for address in addresses:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json"
    response = requests.get(geocoder_request)

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    code = toponym['metaDataProperty']['GeocoderMetaData']['Address'][
        'postal_code']

    print(f'{address} - почтовый индекс: {code}')
