import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

def greedy_best_first_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    came_from = {}
    came_from[start] = None

    while open_list:
        current_heuristic, current_node = heapq.heappop(open_list)
        
        print(f"Visitando: {current_node}")
        
        if current_node == goal:
            print(f"Objetivo {goal} alcançado!")
            break

        for neighbor in graph[current_node]:
            if neighbor not in came_from:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                came_from[neighbor] = current_node

    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = came_from[current_node]
    path.reverse()

    return path

def get_valid_city(prompt):
    valid_cities = ['A', 'B', 'C', 'D', 'E', 'F']
    while True:
        city = input(prompt).upper()
        if city in valid_cities:
            return city
        else:
            print(f"Entrada inválida. Escolha entre {valid_cities}")

start = get_valid_city("Ponto de partida (A, B, C, D, E, F): ")
goal = get_valid_city("Objetivo (A, B, C, D, E, F): ")

path = greedy_best_first_search(graph, heuristic, start, goal)
print(f"Caminho encontrado: {path}")
