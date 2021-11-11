# LINKS REFERENCIAS
# - https://newbedev.com/how-to-iterate-over-files-in-a-given-directory

import sys
import os
from main import get_shortest_path


tests_directory = r'.\tests'
output_filename = tests_directory + "\output.txt"
output_data = []

with open(output_filename, "r") as input_file:
    for out_line in input_file:
        line_data = out_line.strip().split(";")
        output_data.append(line_data)

print("\n")

test_counter = 0
for filename in os.listdir(tests_directory):
    if filename.endswith("test.txt"):
        file_path = os.path.join(tests_directory, filename)
        print(
            f"================ TEST AUTOMÁTICO {test_counter+1} ================")
        tren_sin_color_test = get_shortest_path(file_path, 'A', 'B', '')
        tren_rojo_test = get_shortest_path(file_path, 'A', 'B', '0')
        tren_verde_test = get_shortest_path(file_path, 'A', 'B', '1')

        if tren_sin_color_test == output_data[test_counter][0]:
            print("TEST: Tren sin color: CORRECTO")
        else:
            print("TEST: Tren sin color: INCORRECTO")

        if tren_rojo_test == output_data[test_counter][1]:
            print("TEST: Tren rojo: CORRECTO")
        else:
            print("TEST: Tren rojo: INCORRECTO")

        if tren_verde_test == output_data[test_counter][2]:
            print("TEST: Tren verde: CORRECTO")
        else:
            print("TEST: Tren verde: INCORRECTO")
        print("===================================================")
        print("\n")

    else:
        continue
    test_counter += 1
