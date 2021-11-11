# TAREA DE SELECCIÓN | Buda.com - Metro

# LINKS REFERENCIAS
# - https://pencilprogrammer.com/algorithms/shortest-path-in-unweighted-graph-using-bfs/
# - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# - https://docs.pytest.org/en/6.2.x/

import sys
from classes import Node, ShortestPath

not_reacheble_error = "Los valores ingresados generan una ruta no alcanzable"
color_error = "Se ingresó un valor para el color del tren incorrecto, por favor inténtelo de nuevo"


# *** Poblar el sistema desde input ***
def get_shortest_path(file_name, start_node, end_node, train_color):

    # Estructuras para almacenamiento de datos de red de metro
    nodes_data = dict()
    all_node_name = []

    # Procesamiento archivo input
    with open(file_name, "r") as input_file:
        for line in input_file:
            line_data = line.strip().split(";")
            node_data = line_data[0].split(",")
            neighbors_data = line_data[1].split(",")
            station_node = Node(node_data[0], node_data[1])
            nodes_data[station_node.name] = [station_node, neighbors_data]
            all_node_name.append(node_data[0])

    # Manejo del color del tren
    if train_color == '':
        train_color = "SinColor"
    elif train_color == '0':
        train_color = "Rojo"
    elif train_color == '1':
        train_color = "Verde"
    else:
        return color_error

    # Diccionario con nodos
    graph_station = dict()
    for node_name in all_node_name:
        curr_node = nodes_data[node_name][0]
        neighbor_nodes = nodes_data[node_name][1]
        for nei_node_name in neighbor_nodes:
            if nei_node_name:
                neighbor_node = nodes_data[nei_node_name][0]
                curr_node.neighbors.append(neighbor_node)
        graph_station[node_name] = curr_node

    # Caso en que tren tiene color
    if (train_color != "SinColor") and (train_color != "ColorError"):
        for node_name in all_node_name:
            if (graph_station[node_name].color == train_color) or (graph_station[node_name].color == "SinColor"):
                new_neighbors = []
                other_neighbors = []
                # Copia de vecinos a recorrer
                other_neighbors.extend(graph_station[node_name].neighbors)
                for nn_i in range(len(other_neighbors)):
                    if (other_neighbors[nn_i].color != train_color) and (other_neighbors[nn_i].color != "SinColor"):
                        new_neighbors.extend(other_neighbors[nn_i].neighbors)
                        graph_station[node_name].neighbors.pop(0)

                for new_i in new_neighbors:
                    if new_i.name != node_name:
                        graph_station[node_name].neighbors.append(new_i)

            elif (graph_station[node_name].color != train_color) and (graph_station[node_name].color != "SinColor"):
                del graph_station[node_name]

    shortest_path_class = ""
    try:

        shortest_path_class = ShortestPath(graph_station[start_node.upper()],
                                           graph_station[end_node.upper()])

        shortest_path_class.bfs()
        return shortest_path_class.shortest_path

    except:
        shortest_path_class = not_reacheble_error
        return shortest_path_class


if __name__ == '__main__':

    # Recepción de parámetros
    file_name = sys.argv[1]
    all_node_name = []
    with open(file_name, "r") as input_file:
        for line in input_file:
            line_data = line.strip().split(";")
            node_data = line_data[0].split(",")
            all_node_name.append(node_data[0])

    print("\n")
    print("Elige una estación de inicio y una de término de las que aparecen a continuación: ")
    all_node_names_text = ""
    for i_node in range(len(all_node_name)):
        if i_node + 1 == len(all_node_name):
            all_node_names_text += f"{all_node_name[i_node]}"
        else:
            all_node_names_text += f"{all_node_name[i_node]}, "
    print("\n")
    print(all_node_names_text)
    print("\n")
    start_node = input("Ingrese estación de inicio: ")
    end_node = input("Ingrese estación de término: ")
    train_color = input(
        "Ingrese un color de tren (0: Rojo, 1: Verde), sino presione 'Enter' para continuar: ")

    # Calcular ruta más corta
    shortest_path = get_shortest_path(
        file_name, start_node, end_node, train_color)
    if (shortest_path != not_reacheble_error) and (shortest_path != color_error):
        print("\n")
        print("La ruta más corta es: " + shortest_path)
        print("\n")
    else:
        print("\n")
        print(shortest_path)
        print("\n")
