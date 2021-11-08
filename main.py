# TAREA DE SELECCIÓN - BUDA

# REFERENCIAS
# - https://pencilprogrammer.com/algorithms/shortest-path-in-unweighted-graph-using-bfs/

# class Node de grafo de estaciones
class Node:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.prev = None
        self.neighbors = []
        self.visited = False

    # Método para conectar nodos
    def add_neighbor(self, node):
        self.neighbors.append(node)
        node.neighbors.append(self)

    # Representación de un nodo
    def __repr__(self):
        return self.name


# class ShortestPath para represtar el camino más corto
class ShortestPath:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_route(self, route_list):
        route_text = ""
        for i_node in range(len(route_list)):
            if i_node + 1 == len(route_list):
                route_text += f"{route_list[i_node].name}"
            else:
                route_text += f"{route_list[i_node].name} -> "
        print("\n")
        print("La ruta más corta es: " + route_text)

    def bfs(self):
        # Crear una cola
        queue = []
        # Visitar y agregar de inicio a la cola
        self.start.visited = True
        queue.append(self.start)

        # BFS hasta que la cola se vacíe
        while queue:
            # Pop a un nodo de la cola queue para búsqueda
            current_node = queue.pop(0)
            # Loop por los nodos vecinos hasta encontrar el término
            for node in current_node.neighbors:
                if not node.visited:
                    # Visitar y agregar vecinos a la cola
                    node.visited = True
                    queue.append(node)
                    # Actualizar su nodo predecesor
                    node.prev = current_node
                    # Terminar búsqueda BFS si el nodo visitado es el nodo de término
                    if node == self.end:
                        queue.clear()
                        break
        # BFS completado, ahora recorrer la ruta
        self.trace_route()

    # Función para recorrer la ruta utilizando nodos predecesores
    def trace_route(self):
        node = self.end
        route = []
        # Iniciar con nodo sin predecesor
        # Loop hasta que node->prev sea null
        while node:
            route.append(node)
            node = node.prev
        # Revertir la ruta para traer el inicio al frente
        route.reverse()
        # Output de ruta
        self.print_route(route)


# *** Poblar el sistema desde input ***
nodes_data = dict()
all_node_name = []
with open("input.txt", "r") as input_file:
    for line in input_file:
        line_data = line.strip().split(";")
        node_data = line_data[0].split(",")
        neighbors_data = line_data[1].split(",")
        station_node = Node(node_data[0], node_data[1])
        nodes_data[station_node.name] = [station_node, neighbors_data]
        all_node_name.append(node_data[0])

# print(nodes_data)

# *** Recibir parámetros ***
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
    "(Opcional) Ingrese un color de tren (0: Rojo, 1: Verde): ")

if train_color == '':
    train_color = "SinColor"

else:
    if train_color == '0':
        train_color = "Rojo"
    elif train_color == '1':
        train_color = "Verde"
    else:
        print("Se ingresó un valor para el color del tren incorrecto, por favor inténtelo de nuevo.")


# *** Crear diccionario con nodos ***
graph_station = dict()
for node_name in all_node_name:
    curr_node = nodes_data[node_name][0]
    neighbor_nodes = nodes_data[node_name][1]
    for nei_node_name in neighbor_nodes:
        if nei_node_name:
            neighbor_node = nodes_data[nei_node_name][0]
            curr_node.neighbors.append(neighbor_node)
    graph_station[node_name] = curr_node

# *** Caso en que tren tiene color ***
if train_color != "SinColor":
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

try:
    ShortestPath(graph_station[start_node.upper()],
                 graph_station[end_node.upper()]).bfs()
except:
    print("Los valores ingresados en las estaciones y/o el color del tren, genera una ruta que no es alcanzable")
