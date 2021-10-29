# TAREA DE SELECCIÓN - BUDA

# PARÁMETROS
# archivo input
# Una estación inicial
# Una estación final
# Un color de tren Rojo o Verde (opcional)

############################################################
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
        print(route)


# Poblar el sistema desde input
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


graph_station = dict()
for node_name in all_node_name:
    curr_node = nodes_data[node_name][0]
    neighbor_nodes = nodes_data[node_name][1]
    for nei_node_name in neighbor_nodes:
        if nei_node_name:
            neighbor_node = nodes_data[nei_node_name][0]
            curr_node.add_neighbor(neighbor_node)
    graph_station[node_name] = curr_node

# for node_name in all_node_name:
#     print(node_name)
#     checking_nodes = graph_station[node_name].neighbors
#     print(checking_nodes)

# Recibir parámetros
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
node_color = input("(Opcional) Ingrese estación un color: ")
if node_color == '':
    node_color = "SinColor"


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
ShortestPath(graph_station[start_node], graph_station[end_node]).bfs()
############################################################

# CASOS BORDES
# - No puedo partir desde la última estación.

# OUTPUT
# Y tener como resultado la menor ruta según los parámetros, indicando todas las estaciones
# que la componen. En caso de que haya más de una, basta con que se retorne una
# cualquiera como resultado.


# REFERENCIAS
# - https://pencilprogrammer.com/algorithms/shortest-path-in-unweighted-graph-using-bfs/
