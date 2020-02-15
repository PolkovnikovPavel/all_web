from distance import lonlat_distance
import requests


address_1 = input()
address_2 = input()

url = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address_1}&format=json'
response = requests.get(url)
json_response = response.json()
address_ll_1 = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]['Point']['pos']
address_ll_1 = list(map(float, address_ll_1.split()))

url = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address_2}&format=json'
response = requests.get(url)
json_response = response.json()
address_ll_2 = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]['Point']['pos']
address_ll_2 = list(map(float, address_ll_2.split()))

print(f'{int(lonlat_distance(address_ll_1, address_ll_2))}м.')
