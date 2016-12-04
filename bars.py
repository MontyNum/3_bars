import json


def load_data(filepath):
    return json.load(open(filepath, 'r'))


def get_biggest_bar(data):
    bars = [(bar['SeatsCount'], bar['Name']) for bar in data]
    return [name for cnt, name in bars if cnt == max(bars)[0]]


def get_smallest_bar(data):
    bars = [(bar['SeatsCount'], bar['Name']) for bar in data]
    return [name for cnt, name in bars if cnt == min(bars)[0]]


def get_closest_bar(data, longitude, latitude):
    '''Евклидовы расстояния'''
    bars = [((bar['geoData']['coordinates'][0]-longitude)**2 + (bar['geoData']['coordinates'][1]-latitude)**2, bar['Name']) \
            for bar in data]
    return min(bars)[1]


if __name__ == '__main__':
    pass
