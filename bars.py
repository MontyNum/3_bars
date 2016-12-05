import json


def load_data(filepath):
    import os
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    bars = [(bar['SeatsCount'], bar['Name']) for bar in data]
    return [name for cnt, name in bars if cnt == max(bars)[0]]


def get_smallest_bar(data):
    bars = [(bar['SeatsCount'], bar['Name']) for bar in data]
    return [name for cnt, name in bars if cnt == min(bars)[0]]


def get_closest_bar(data, longitude, latitude):
    '''
    -90 <= longitude <= 90
    -180 <= latitude <= 180
    '''
    bars = [([abs(bar['geoData']['coordinates'][0]-longitude), abs(bar['geoData']['coordinates'][1]-latitude)], bar['Name']) \
            for bar in data]
    distance = []
    for angles, name in bars:
        if angles[1]>180.:                                   # carefully
            angles[1] = 360. - angles[1]
        distance.append((angles[0]**2 + angles[1]**2, name)) # square of angle distance
    return [name for dist, name in distance if dist == min(distance)[0]]


if __name__ == '__main__':
    pass
