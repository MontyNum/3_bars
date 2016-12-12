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

def get_bar_seat_counts(bars_content):
    bar_seat_counts = [(bar['SeatsCount'], bar['Name']) for bar in bars_content]
    return bar_seat_counts

def get_biggest_bar(bars_content):
    bar_seat_counts = get_bar_seat_counts(bars_content)
    # Не понимаю зачем импользовать key: его использование уместно только если функция должна будет возвращать ОДИН единственный бар,
    # но в данных присутствуют бары, с одинаковым максимальным кол-ом посадочных мест. Поэтому моя фунция возвращает список баров с
    # предельным значением 'SeatsCount' и, как я думаю, это не сделать одним единственным использованием key. Я в тупике...
    biggest_bars = [bar_name for bar_seat_count, bar_name in bar_seat_counts if bar_seat_count == max(bar_seat_counts)[0]]
    return biggest_bars


def get_smallest_bar(bars_content):
    bar_seat_counts = get_bar_seat_counts(bars_content)
    smallest_bars = [bar_name for bar_seat_count, bar_name in bar_seat_counts if bar_seat_count == min(bar_seat_counts)[0]]
    return smallest_bars


def get_bars_coordinates(bars_content):
    bars_coordinates = [([abs(bar['geoData']['coordinates'][0] - longitude), abs(bar['geoData']['coordinates'][1] - latitude)], \
                         bar['Name']) for bar in bars_content]
    return bars_coordinates


def get_angle_distances(bars_coordinates, longitude, latitude):
    distances = []
    for bar_coordinates, bar_name in bars_coordinates:
        if bar_coordinates[1] > 180.:                                    
            bar_coordinates[1] = 360. - bar_coordinates[1]
        distances.append((bar_coordinates[0]**2 + bar_coordinates[1]**2, bar_name)) 
    return distances
        
        
def get_closest_bar(bars_content, longitude, latitude):
    bars_coordinates = get_bars_coordinates(bars_content)
    angle_distances = get_angle_distances(bars_coordinates, longitude, latitude)
    closest_bars = [bar_name for bar_distance, bar_name in angle_distances if bar_distance == min(angle_distances)[0]]
    return closest_bars


if __name__ == '__main__':
    file_path = input('Enter path of file: ')
    bars_content = load_data_of_bars(file_path)
    print('\nThe biggest bar:', get_biggest_bar(bars_content))
    print('The smallest bar:', get_smallest_bar(bars_content), '\n')
    longitude = float(input('Enter longitude of interesting position: '))
    latitude = float(input('Enter latitude of interesting position: '))
    print('\nThe closest bar:', get_closest_bar(bars_content, longitude, latitude))
