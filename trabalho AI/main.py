import tkinter as tk
from tkinter import ttk
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        if current_node == goal:
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

def draw_graph(path):
    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    plt.clf()
    pos = nx.circular_layout(G)
    num_nodes = len(G.nodes())
    node_colors = plt.colormaps['tab20'](range(num_nodes))
    edge_colors = ['#333333' if node not in path else '#FF5733' for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_weight='bold',
            node_color=node_colors, edge_color=edge_colors, linewidths=1.5)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    plt.title('Gráfico de Caminho', fontsize=14)
    plt.axis('off')

root = tk.Tk()
root.title("Busca Gulosa melhor caminho")

ttk.Label(root, text="Busca Gulosa melhor caminho").pack(pady=10)
origin_var = tk.StringVar()
destination_var = tk.StringVar()
result_var = tk.StringVar()

frame_graph = tk.Frame(root)
frame_graph.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

frame_controls = tk.Frame(root)
frame_controls.pack(side=tk.RIGHT, fill=tk.Y)

ttk.Label(frame_controls, text="Origem:").pack(pady=10)
origin_combobox = ttk.Combobox(frame_controls, textvariable=origin_var, values=list(graph.keys()))
origin_combobox.pack(pady=5)
origin_combobox.current(0)

ttk.Label(frame_controls, text="Destino:").pack(pady=10)
destination_combobox = ttk.Combobox(frame_controls, textvariable=destination_var, values=list(graph.keys()))
destination_combobox.pack(pady=5)
destination_combobox.current(1)

search_button = ttk.Button(frame_controls, text="Buscar", command=lambda: on_search())
search_button.pack(pady=20)

ttk.Label(frame_controls, text="Melhor caminho:").pack(pady=10)
result_label = ttk.Label(frame_controls, textvariable=result_var, wraplength=200)
result_label.pack(pady=5)

def on_search():
    start = origin_var.get()
    goal = destination_var.get()
    path = greedy_best_first_search(graph, heuristic, start, goal)
    draw_graph(path)
    canvas.draw()
    result_var.set(" → ".join(path))

root.mainloop()

pip install networkx matplotlib
