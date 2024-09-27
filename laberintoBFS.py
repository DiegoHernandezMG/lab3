from collections import deque

def is_valid_move(maze, position, visited):
    row, col = position
    # Verificar si la posición está dentro de los límites del laberinto
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        # Verificar si es un camino (0) y no ha sido visitado antes
        return maze[row][col] == 0 and position not in visited
    return False

def bfs_maze(maze, start, end):
    queue = deque([(start, [start])])  # Cola para BFS con tupla (posición actual, camino recorrido)
    visited = set()                    # Conjunto para las posiciones visitadas
    visited.add(start)

    # Direcciones posibles de movimiento: abajo, arriba, derecha, izquierda
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        current, path = queue.popleft()  # Tomamos el primer elemento de la cola
        row, col = current

        # Si hemos llegado a la posición final, retornamos el camino
        if current == end:
            return path

        # Explorar cada dirección
        for dr, dc in directions:
            next_position = (row + dr, col + dc)
            if is_valid_move(maze, next_position, visited):
                visited.add(next_position)  # Marcar como visitada
                queue.append((next_position, path + [next_position]))  # Agregar a la cola

    return "No hay camino posible"  # Si agotamos la cola y no encontramos el final

def solve_maze(maze, start, end):
    return bfs_maze(maze, start, end)

# Definición del laberinto
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

# Posición inicial y final
start = (0, 1)
end = (3, 4)

# Resolver el laberinto
path = solve_maze(maze, start, end)

print("Camino encontrado:" if isinstance(path, list) else path)
print(path)