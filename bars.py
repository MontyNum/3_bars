import json, sys, os


def load_data(filepath):
    if not os.path.exists(filepath):
        print('There is no such path or file. Exiting...')
        sys.exit()
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
    file_path = input('Enter path of file: ')
    data = load_data(file_path)
    print('\nThe biggest bar:', get_biggest_bar(data))
    print('The smallest bar:', get_smallest_bar(data), '\n')
    longitude = float(input('Enter longitude of interesting position: '))
    latitude = float(input('Enter latitude of interesting position: '))
    print('\nThe closest bar:', get_closest_bar(data, longitude, latitude))
