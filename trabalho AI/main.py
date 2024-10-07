# Importa bibliotecas necessárias
import tkinter as tk
from tkinter import ttk
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Comando para instalar a biblioteca:
# pip install networkx matplotlib

## Define o grafo
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

# Define a heurística
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

# Implementa a busca gulosa
def greedy_best_first_search(graph, heuristic, start, goal):
    # Cria a lista de abertos
    open_list = []
    # Adiciona o nodo inicial com a heurística
    heapq.heappush(open_list, (-heuristic[start], start))
    # Cria a lista de fechados
    came_from = {}
    # Adiciona o nodo inicial como fechado
    came_from[start] = None

    # Enquanto houver nodos na lista de abertos
    while open_list:
        # Pega o nodo com a menor heurística
        _, current_node = heapq.heappop(open_list)
        # Se o nodo for o destino, sai do loop
        if current_node == goal:
            break
        # Para cada vizinho do nodo
        for neighbor in graph[current_node]:
            # Se o vizinho ainda não foi visitado
            if neighbor not in came_from:
                # Adiciona o vizinho na lista de abertos com a heurística
                heapq.heappush(open_list, (-heuristic[neighbor], neighbor))
                # Adiciona o vizinho como fechado
                came_from[neighbor] = current_node

    # Cria a lista do caminho
    path = []
    # Pega o nodo atual
    current_node = goal
    # Enquanto houver um nodo
    while current_node is not None:
        # Adiciona o nodo ao caminho
        path.append(current_node)
        # Pega o nodo anterior
        current_node = came_from[current_node]
    # Inverte a ordem do caminho
    path.reverse()
    # Retorna o caminho
    return path

# Implementa a função para desenhar o grafo
def draw_graph(path):
    # Cria o grafo
    G = nx.Graph()
    # Para cada nodo no grafo
    for node in graph:
        # Para cada vizinho do nodo
        for neighbor, weight in graph[node].items():
            # Adiciona a aresta ao grafo
            G.add_edge(node, neighbor, weight=weight)

    # Desenha o grafo
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

# Cria a janela principal
root = tk.Tk()
root.title("Busca Gulosa melhor caminho")

# Cria o label
ttk.Label(root, text="Busca Gulosa melhor caminho").pack(pady=10)
# Cria as variáveis de origem e destino
origin_var = tk.StringVar()
destination_var = tk.StringVar()
# Cria a variável do resultado
result_var = tk.StringVar()

# Cria o frame do grafo
frame_graph = tk.Frame(root)
frame_graph.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Cria o canvas do grafo
fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Cria o frame dos controles
frame_controls = tk.Frame(root)
frame_controls.pack(side=tk.RIGHT, fill=tk.Y)

# Cria o label de origem
ttk.Label(frame_controls, text="Origem:").pack(pady=10)
# Cria o combobox de origem
origin_combobox = ttk.Combobox(frame_controls, textvariable=origin_var, values=list(graph.keys()))
origin_combobox.pack(pady=5)
# Define o valor padrão do combobox
origin_combobox.current(0)

# Cria o label de destino
ttk.Label(frame_controls, text="Destino:").pack(pady=10)
# Cria o combobox de destino
destination_combobox = ttk.Combobox(frame_controls, textvariable=destination_var, values=list(graph.keys()))
destination_combobox.pack(pady=5)
# Define o valor padrão do combobox
destination_combobox.current(1)

# Cria o botão de busca
search_button = ttk.Button(frame_controls, text="Buscar", command=lambda: on_search())
search_button.pack(pady=20)

# Cria o label do resultado
ttk.Label(frame_controls, text="Melhor caminho:").pack(pady=10)
# Cria o label do resultado
result_label = ttk.Label(frame_controls, textvariable=result_var, wraplength=200)
result_label.pack(pady=5)

# Implementa a função para quando o botão de busca for pressionado
def on_search():
    start = origin_var.get()
    goal = destination_var.get()
    path = greedy_best_first_search(graph, heuristic, start, goal)
    draw_graph(path)
    canvas.draw()
    result_var.set(" → ".join(path))

# Inicia o loop principal
root.mainloop()

