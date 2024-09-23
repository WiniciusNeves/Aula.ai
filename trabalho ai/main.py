import heapq

# Grafo das cidades com as distâncias entre elas
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# Estimativa heurística das distâncias em linha reta até o objetivo (cidade 'F')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

# Função de busca gulosa de melhor escolha
def greedy_best_first_search(graph, heuristic, start, goal):
    # Usamos uma fila de prioridade para expandir o nó com menor heurística
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    # Para manter o caminho que estamos seguindo
    came_from = {}
    came_from[start] = None

    while open_list:
        # Pegamos o nó com menor valor heurístico
        current_heuristic, current_node = heapq.heappop(open_list)
        
        print(f"Visitando: {current_node}")
        
        # Verificamos se chegamos ao objetivo
        if current_node == goal:
            break

        # Expandimos os vizinhos
        for neighbor in graph[current_node]:
            if neighbor not in came_from:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                came_from[neighbor] = current_node

    # Reconstruindo o caminho
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = came_from[current_node]
    path.reverse()

    return path

# Definimos o ponto de partida e o objetivo
start = 'A'
goal = 'E'

# Executamos a busca gulosa
path = greedy_best_first_search(graph, heuristic, start, goal)
print(f"Caminho encontrado: {path}")

