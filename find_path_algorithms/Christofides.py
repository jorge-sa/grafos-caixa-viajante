import numpy as np
import networkx as nx
from tkinter import filedialog as fd

def open_file_selection():
    return fd.askopenfile()

# Construir matriz de distâncias entre cidades
def build_graph_matrix():
    file = open_file_selection()

    dist_matrix = []
    for line in file:
        row = [float(x) for x in line.split()]
        dist_matrix.append(row)
    file.close()

    return dist_matrix

# Função para encontrar a árvore de abrangência mínima usando o algoritmo de Prim
def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)

# Função para encontrar os vértices com grau ímpar
def find_odd_vertices(graph):
    odd_vertices = []
    for node in graph.nodes():
        if graph.degree(node) % 2 != 0:
            odd_vertices.append(node)
    return odd_vertices

# Função para encontrar o casamento perfeito de peso mínimo dos vértices ímpares usando algoritmo guloso
def minimum_weight_matching(graph, odd_vertices):
    min_weight_matching = nx.algorithms.matching.max_weight_matching(graph, maxcardinality=False)
    min_weight_matching_edges = [(u, v) for u, v in min_weight_matching]
    return min_weight_matching_edges

# Função para construir um multigrafo a partir da árvore de abrangência mínima e do casamento de peso mínimo
def construct_multigraph(graph, mst, matching_edges):
    multigraph = nx.MultiGraph(graph)
    multigraph.add_edges_from(matching_edges)
    return multigraph

# Função para encontrar um circuito euleriano no multigrafo
def eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))

# Função para encontrar um circuito hamiltoniano a partir do circuito euleriano
def christofides_algorithm(graph):
    # Passo 1: Calcular a árvore de abrangência mínima
    mst = minimum_spanning_tree(graph)

    # Passo 2: Encontrar vértices com grau ímpar
    odd_vertices = find_odd_vertices(mst)

    # Passo 3: Encontrar casamento perfeito de peso mínimo dos vértices ímpares
    min_weight_matching_edges = minimum_weight_matching(graph, odd_vertices)

    # Passo 4: Construir um multigrafo
    multigraph = construct_multigraph(graph, mst, min_weight_matching_edges)

    # Passo 5: Encontrar um circuito euleriano no multigrafo
    eulerian_path = eulerian_circuit(multigraph)

    # Passo 6: Remover duplicatas do caminho euleriano para obter um caminho hamiltoniano
    hamiltonian_path = list(dict.fromkeys([node for node, _ in eulerian_path]))

    # Passo 7: Retornar o circuito hamiltoniano
    return hamiltonian_path

# Exemplo de uso:
if __name__ == "__main__":
    # Construir matriz de grafo
    graph_matrix = build_graph_matrix()

    # Converter matriz em grafo
    graph = nx.from_numpy_array(np.array(graph_matrix))

    # Executar algoritmo de Christofides
    hamiltonian_path = christofides_algorithm(graph)

    print("Solução aproximada (circuito hamiltoniano):", hamiltonian_path)
