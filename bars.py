import json
import sys
import os


def load_data_of_bars(json_filepath):
    if not os.path.exists(json_filepath):
        print('There is no such path or file. Exiting...')
        sys.exit()
    with open(json_filepath, 'r') as file_handler:
        bars_content = json.load(file_handler)
        return bars_content


def get_biggest_bar(bars_content):
    biggest_bar_info = max(bars_content, key=lambda bar_info: bar_info['SeatsCount'])
    return biggest_bar_info['Name']


def get_smallest_bar(bars_content):
    smallest_bar_info = min(bars_content, key=lambda bar_info: bar_info['SeatsCount'])
    return smallest_bar_info['Name']



def get_angle_distance(bar_info, longitude, latitude):
    bar_info['geoData']['coordinates'][0] -= longitude
    latitude_distance = abs(bar_info['geoData']['coordinates'][1] - latitude)
    if latitude_distance > 180.:                                    
        bar_info['geoData']['coordinates'][1] = 360. - latitude_distance
    else:
        bar_info['geoData']['coordinates'][1] = latitude_distance
    return bar_info['geoData']['coordinates'][0]**2 + bar_info['geoData']['coordinates'][1]**2
        
        
def get_closest_bar(bars_content, longitude, latitude):
    closest_bar_info = min(bars_content, key=lambda bar_info: get_angle_distance(bar_info, longitude, latitude))
    return closest_bar_info['Name']


if __name__ == '__main__':
    file_path = input('Enter path of file: ')
    bars_content = load_data_of_bars(file_path)
    print('\nThe biggest bar:', get_biggest_bar(bars_content))
    print('The smallest bar:', get_smallest_bar(bars_content), '\n')
    longitude = float(input('Enter longitude of interesting position: '))
    latitude = float(input('Enter latitude of interesting position: '))
    print('\nThe closest bar:', get_closest_bar(bars_content, longitude, latitude))
