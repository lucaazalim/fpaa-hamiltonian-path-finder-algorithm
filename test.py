import unittest
from hamiltonian import find_hamiltonian_path


class TestHamiltonianPath(unittest.TestCase):

    def test_path_exists_small_graph(self):
        """
        Test a small graph where a Hamiltonian Path exists.
        """
        graph = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        path = find_hamiltonian_path(graph)
        self.assertEqual(len(path), 4)
        self.assertEqual(len(set(path)), 4)  # All vertices are unique

    def test_no_path(self):
        """
        Test a disconnected graph where no Hamiltonian Path exists.
        """
        graph = [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]
        path = find_hamiltonian_path(graph)
        self.assertEqual(path, [])

    def test_single_vertex(self):
        """
        Test a graph with only one vertex.
        """
        graph = [
            [0]
        ]
        path = find_hamiltonian_path(graph)
        self.assertEqual(path, [0])

    def test_invalid_graph_not_square(self):
        """
        Test that a ValueError is raised for a non-square matrix.
        """
        graph = [
            [0, 1],
            [1]
        ]
        with self.assertRaises(ValueError):
            find_hamiltonian_path(graph)

    def test_complete_graph(self):
        """
        Test a complete graph with 5 vertices.
        """
        n = 5
        graph = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
        path = find_hamiltonian_path(graph)
        self.assertEqual(len(path), n)
        self.assertEqual(len(set(path)), n)


if __name__ == "__main__":
    unittest.main()
