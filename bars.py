import json
import sys
import os


def load_data_of_bars(filepath):
    if not os.path.exists(filepath):
        print('There is no such path or file. Exiting...')
        sys.exit()
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(json_content):
    bars = [(bar['SeatsCount'], bar['Name']) for bar in json_content]
    biggest_bars = [bar_name for bar_seats_count, bar_name in bars if bar_seats_count == max(bars)[0]]
    return biggest_bars


def get_smallest_bar(json_content):
    bars = [(bar['SeatsCount'], bar['Name']) for bar in json_content]
    smallest_bars = [bar_name for bar_seats_count, bar_name in bars if bar_seats_count == min(bars)[0]]
    return smallest_bars


def get_closest_bar(json_content, longitude, latitude):
    '''
    -90 <= longitude <= 90
    -180 <= latitude <= 180
    '''
    bars = [([abs(bar['geoData']['coordinates'][0]-longitude), abs(bar['geoData']['coordinates'][1]-latitude)], bar['Name']) \
            for bar in json_content]
    distances = []
    for bar_coordinates, bar_name in bars:
        if bar_coordinates[1] > 180.:                                    # carefully
            bar_coordinates[1] = 360. - bar_coordinates[1]
        distances.append((bar_coordinates[0]**2 + bar_coordinates[1]**2, bar_name)) # square of angle distance
    closest_bars = [bar_name for bar_distance, bar_name in distances if bar_distance == min(distances)[0]]
    return closest_bars


if __name__ == '__main__':
    file_path = input('Enter path of file: ')
    bars = load_data_of_bars(file_path)
    print('\nThe biggest bar:', get_biggest_bar(bars))
    print('The smallest bar:', get_smallest_bar(bars), '\n')
    longitude = float(input('Enter longitude of interesting position: '))
    latitude = float(input('Enter latitude of interesting position: '))
    print('\nThe closest bar:', get_closest_bar(bars, longitude, latitude))
