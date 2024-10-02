import heapq
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 3},
    'E': {'B': 5, 'F': 1, 'H': 4},
    'F': {'C': 3, 'E': 1, 'I': 2},
    'G': {'D': 3, 'J': 6},
    'H': {'E': 4, 'K': 5},
    'I': {'F': 2, 'L': 1},
    'J': {'G': 6},
    'K': {'H': 5},
    'L': {'I': 1}
}

heuristic = {
    'A': 10,
    'B': 9,
    'C': 7,
    'D': 8,
    'E': 6,
    'F': 4,
    'G': 7,
    'H': 5,
    'I': 3,
    'J': 8,
    'K': 4,
    'L': 0
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
    valid_cities = list(graph.keys())
    while True:
        city = input(prompt).upper()
        if city in valid_cities:
            return city

def draw_graph(graph, path):
    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    plt.show()

start = get_valid_city("Ponto de partida: ")
goal = get_valid_city("Objetivo: ")

path = greedy_best_first_search(graph, heuristic, start, goal)
print(f"Caminho encontrado: {path}")

draw_graph(graph, path)
