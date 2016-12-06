# 3_bars
This script provides to compute the bigget bar, the smallest bar and the closest bar of Moscow bars.
The data must have json type (for more details see: http://data.mos.ru/opendata/7710881420-bary).

**load_data(** *filepath* **)** 
  Downloads data.json from file path directory and returns deserialized a Python object.

Function *get_biggest_bar(data)* returns the biggest bar of Moscow.

Function *get_smallest_bar(data)* returns the smallest bar of Moscow.

Function *get_closest_bar(data, longitude, latitude)* receives data (a Python object), longitude and latitude of interesting location. The function returns a list of bars that are the closest to the location (if their distances are equal).
