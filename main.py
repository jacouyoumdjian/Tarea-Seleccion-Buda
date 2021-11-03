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
            # Pop a node from queue for search operation
            current_node = queue.pop(0)
            # Loop through neighbors nodes to find the 'end' node
            for node in current_node.neighbors:
                if not node.visited:
                    # visit and add neighbors nodes to the queue
                    node.visited = True
                    queue.append(node)
                    # update its preceding node
                    node.prev = current_node
                    # stop BFS if the visited node is the end node
                    if node == self.end:
                        queue.clear()
                        break
        # BFS completed, now trace the route
        self.trace_route()

    # Function to trace the route using preceding nodes
    def trace_route(self):
        node = self.end
        route = []
        # start node has no preceding node
        # so loop until node->prev is null
        while node:
            route.append(node)
            node = node.prev
        # reverse the route bring start to the front
        route.reverse()
        # output route
        self.print_route(route)


# *** Poblar el sistema desde input ***
nodes_data = dict()
all_node_name = []
with open("input3.txt", "r") as input_file:
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
train_color = input("(Opcional) Ingrese un color de tren: ")
if train_color == '':
    train_color = "SinColor"

# *** Crear dict ordenado con nodos ***
graph_station = dict()
for node_name in all_node_name:
    curr_node = nodes_data[node_name][0]
    neighbor_nodes = nodes_data[node_name][1]
    for nei_node_name in neighbor_nodes:
        if nei_node_name:
            neighbor_node = nodes_data[nei_node_name][0]
            curr_node.neighbors.append(neighbor_node)
    graph_station[node_name] = curr_node


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

ShortestPath(graph_station[start_node], graph_station[end_node]).bfs()


# BORRADORES
# if __name__ == '__main__':
#     # create nodes
#     node_A = Node('A')
#     node_B = Node('B')
#     node_C = Node('C')
#     node_D = Node('D')
#     node_E = Node('E')
#     # connect nodes (i.e. create graph)
#     node_A.add_neighbor(node_B)
#     node_B.add_neighbor(node_C)
#     node_C.add_neighbor(node_D)
#     node_D.add_neighbor(node_E)
#     node_B.add_neighbor(node_E)

#     ShortestPath(node_A, node_E).bfs()
