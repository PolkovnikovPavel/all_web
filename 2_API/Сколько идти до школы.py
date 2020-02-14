import math
import requests


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


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
