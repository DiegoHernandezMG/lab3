from estructuras import Cola, ListaGenerica

def bfs_4_puzzle(estado_inicial, estado_objetivo):
    frontera = Cola()  # Cola para los nodos frontera
    visitados = ListaGenerica()  # Lista de nodos visitados

    # Insertamos el estado inicial en la frontera y en visitados
    frontera.insertar((estado_inicial, []))  # Guardamos también el camino tomado hasta este punto
    visitados.insertar(estado_inicial)

    while not frontera.is_empty():
        # Extraemos el primer nodo de la frontera
        estado_actual, camino = frontera.quitar()

        # Si es el estado objetivo, hemos terminado
        if estado_actual == estado_objetivo:
            print("¡Solución encontrada!")
            print("Camino a la solución:", camino + [estado_actual])
            return camino + [estado_actual]

        # Generamos los posibles movimientos del estado actual
        for vecino in generar_movimientos(estado_actual):
            if not visitados.buscar(vecino):
                # Añadimos el vecino a la frontera con el camino actualizado
                frontera.insertar((vecino, camino + [estado_actual]))
                visitados.insertar(vecino)

    print("No se encontró solución.")
    return None

# Función para generar los posibles movimientos del puzzle
def generar_movimientos(estado):
    movimientos = []
    # Aquí debes definir cómo se generan los estados vecinos (intercambiar elementos en el puzzle)
    # Ejemplo simple: intercambiar posiciones adyacentes
    for i in range(len(estado) - 1):
        nuevo_estado = estado[:]
        nuevo_estado[i], nuevo_estado[i + 1] = nuevo_estado[i + 1], nuevo_estado[i]
        movimientos.append(nuevo_estado)
    return movimientos

# Ejemplo de uso
if __name__ == "__main__":
    estado_inicial = [1, 4, 3, 2]
    estado_objetivo = [1, 2, 3, 4]

    bfs_4_puzzle(estado_inicial, estado_objetivo)
