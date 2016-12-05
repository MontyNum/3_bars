import json
import sys
import os


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
    
    longitude = None
    while not longitude:
        try:
            longitude = float(input('Enter longitude of interesting position: '))
        except ValueError:
            print('It is not a number. Exiting...')
            sys.exit()
        if longitude > 90. or longitude < - 90.:
            print('Longitude must lie within [-90;90]')
            longitude = None
            
    latitude = None
    while not latitude:
        try:
            latitude = float(input('Enter latitude of interesting position: '))
        except ValueError:
            print('It is not a number. Exiting...')
            sys.exit()
        if latitude > 180. or latitude < -180.:
            print('Latitude must lie within [-180;180]')
            latitude = None
            
    print('\nThe closest bar:', get_closest_bar(data, longitude, latitude))
