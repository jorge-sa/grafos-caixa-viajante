import numpy as np
import networkx as nx
from tkinter import filedialog as fd

def open_file_selection():
    return fd.askopenfile()

# Build cities distance matrix
def build_graph_matrix():
    file = open_file_selection()

    dist_matrix = []
    for line in file:
        row = [float(x) for x in line.split()]
        dist_matrix.append(row)
    file.close()

    return dist_matrix

# Function to find the minimum spanning tree using Prim's algorithm
def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)

# Function to find the vertices with odd degree
def find_odd_vertices(graph):
    odd_vertices = []
    for node in graph.nodes():
        if graph.degree(node) % 2 != 0:
            odd_vertices.append(node)
    return odd_vertices

# Function to find the minimum weight perfect matching of odd vertices using greedy algorithm
def minimum_weight_matching(graph, odd_vertices):
    min_weight_matching = nx.algorithms.matching.max_weight_matching(graph, maxcardinality=False)
    min_weight_matching_edges = [(u, v) for u, v in min_weight_matching]
    return min_weight_matching_edges

# Function to construct a multigraph from the minimum spanning tree and minimum weight matching
def construct_multigraph(graph, mst, matching_edges):
    multigraph = nx.MultiGraph(graph)
    multigraph.add_edges_from(matching_edges)
    return multigraph

# Function to find an Eulerian circuit in the multigraph
def eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))

# Function to find a Hamiltonian circuit from the Eulerian circuit
def christofides_algorithm(graph):
    # Step 1: Compute minimum spanning tree
    mst = minimum_spanning_tree(graph)

    # Step 2: Find vertices with odd degree
    odd_vertices = find_odd_vertices(mst)

    # Step 3: Find minimum weight perfect matching of odd vertices
    min_weight_matching_edges = minimum_weight_matching(graph, odd_vertices)

    # Step 4: Construct a multigraph
    multigraph = construct_multigraph(graph, mst, min_weight_matching_edges)

    # Step 5: Find Eulerian circuit in multigraph
    eulerian_path = eulerian_circuit(multigraph)

    # Step 6: Remove duplicates from Eulerian path to get Hamiltonian path
    hamiltonian_path = list(dict.fromkeys([node for node, _ in eulerian_path]))

    # Step 7: Return the Hamiltonian circuit
    return hamiltonian_path

# Example usage:
if __name__ == "__main__":
    # Build graph matrix
    graph_matrix = build_graph_matrix()

    # Convert matrix to graph
    graph = nx.from_numpy_array(np.array(graph_matrix))

    # Run Christofides algorithm
    hamiltonian_path = christofides_algorithm(graph)

    print("Approximate solution (Hamiltonian circuit):", hamiltonian_path)
