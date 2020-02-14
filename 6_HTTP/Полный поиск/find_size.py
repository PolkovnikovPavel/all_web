def get_with_height_object(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    upper = toponym['boundedBy']['Envelope']['upperCorner'].split()
    point = toponym['Point']['pos'].split()

    w = abs(float(upper[0]) - float(point[0]))
    h = abs(float(upper[1]) - float(point[1]))
    return w, h
