from hamiltonian import find_hamiltonian_path
import matplotlib.pyplot as plt
import networkx as nx
from typing import List

def draw_graph_with_hamiltonian_path(graph: List[List[int]], path: List[int]):
    G = nx.Graph()
    n = len(graph)

    # Add nodes and edges
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G, seed=42)

    # Draw full graph
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=700, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): f'{i}-{j}' for i, j in G.edges()}, font_color='black')

    # Highlight Hamiltonian Path
    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    plt.title("Graph with Hamiltonian Path" if path else "Graph without Hamiltonian Path")
    plt.show()

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    ]

    path = find_hamiltonian_path(graph)
    print("Hamiltonian Path found:" if path else "No Hamiltonian Path found.")
    print(path)

    draw_graph_with_hamiltonian_path(graph, path)