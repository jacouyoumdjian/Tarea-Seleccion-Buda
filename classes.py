# Clase Node de grafo de estaciones
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


# Clase ShortestPath para representar el camino más corto
class ShortestPath:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.shortest_path = ""

    # Método de búsqueda de ruta más corta
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

    # Método para recorrer la ruta utilizando nodos predecesores
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
        # Impresión de ruta
        route_text = ""
        for i_node in range(len(route)):
            if i_node + 1 == len(route):
                route_text += f"{route[i_node].name}"
            else:
                route_text += f"{route[i_node].name} -> "
        self.shortest_path = route_text
