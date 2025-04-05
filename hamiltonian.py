from typing import List

def find_hamiltonian_path(graph: List[List[int]]) -> List[int]:
    """
    Find a Hamiltonian Path in the given graph, if one exists.

    :param graph: A square adjacency matrix representing the graph (0s and 1s).
    :return: A list of vertices representing the Hamiltonian Path, or an empty list if none exists.
    :raises ValueError: If the input graph is not a square matrix.
    """
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Input graph must be a square adjacency matrix.")

    path = [-1] * n
    path[0] = 0 # Start path from vertex 0

    if not backtrack(graph, path, 1):
        return []

    return path

def backtrack(graph: List[List[int]], path: List[int], position: int) -> bool:
    """
    Recursive helper function that attempts to build a Hamiltonian Path using backtracking.

    :param graph: The adjacency matrix representing the graph.
    :param path: The current Hamiltonian Path being constructed.
    :param position: The current index in the path to be filled.
    :return: True if a valid Hamiltonian Path is found, False otherwise.
    """
    if position == len(graph):
        return True

    for vertex in range(1, len(graph)):
        if is_valid(vertex, graph, path, position):
            path[position] = vertex

            if backtrack(graph, path, position + 1):
                return True

            path[position] = -1 # Backtrack

    return False

def is_valid(vertex: int, graph: List[List[int]], path: List[int], position: int) -> bool:
    """
    Check whether a given vertex can be added at the current position in the path.

    :param vertex: The vertex being considered for inclusion in the path.
    :param graph: The adjacency matrix representing the graph.
    :param path: The current path being constructed.
    :param position: The index in the path where the vertex is to be added.
    :return: True if the vertex can be added, False otherwise.
    """
    if graph[path[position - 1]][vertex] == 0:
        return False # No edge between last vertex in path and current vertex

    if vertex in path:
        return False # Vertex is already in path

    return True