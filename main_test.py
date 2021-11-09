# LINKS REFERENCIAS
# - https://newbedev.com/how-to-iterate-over-files-in-a-given-directory

import sys
import os
# from classes import Node, ShortestPath
from main import get_shortest_path


tests_directory = r'.\tests'
for filename in os.listdir(tests_directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(tests_directory, filename)
        print(file_path)

        # tren_sin_color_test = get_shortest_path(file_path, 'A', 'B', '')
        # tren_rojo_test = get_shortest_path(file_path, 'A', 'B', '0')
        # tren_verde_test = get_shortest_path(file_path, 'A', 'B', '1')

    else:
        continue
