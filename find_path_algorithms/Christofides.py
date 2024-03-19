import tkinter as tk
from tkinter import filedialog

def ler_arquivo():
    arquivo = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo",
                                         filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")))
    try:
        with open(arquivo, 'r') as f:
            # Ler linhas do arquivo
            linhas = f.readlines()
            # Processar as linhas para criar uma matriz de números
            dados = [list(map(int, linha.strip().split())) for linha in linhas]
            tsp(dados)  # Chamando a função tsp com a matriz lida do arquivo
    except FileNotFoundError:
        print("Arquivo não encontrado")

def tsp(data):
    G = build_graph(data)
    print("Grafo: ", G)

    MSTree = minimum_spanning_tree(G)
    print("Árvore de Espalhamento Mínimo: ", MSTree)

    odd_vertexes = find_odd_vertexes(MSTree)
    print("Vértices ímpares na Árvore de Espalhamento Mínimo: ", odd_vertexes)

    minimum_weight_matching(MSTree, G, odd_vertexes)
    print("Emparelhamento de peso mínimo: ", MSTree)

    eulerian_tour = find_eulerian_tour(MSTree, G)

    print("Circuito Euleriano: ", eulerian_tour)

    current = eulerian_tour[0]
    path = [current]
    visited = [False] * len(eulerian_tour)
    visited[eulerian_tour[0]] = True
    length = 0

    for v in eulerian_tour:
        if not visited[v]:
            path.append(v)
            visited[v] = True
            length += G[current][v]
            current = v

    length += G[current][eulerian_tour[0]]
    path.append(eulerian_tour[0])

    print("Caminho resultante: ", path)
    print("Comprimento do caminho resultante: ", length)

    return length, path

def build_graph(data):
    graph = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i not in graph:
                graph[i] = {}
            graph[i][j] = data[i][j]
    return graph

class UnionFind:
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        return iter(self.parents)

    def union(self, *objects):
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

def minimum_spanning_tree(G):
    tree = []
    subtrees = UnionFind()
    for u in range(len(G)):
        for v in range(len(G[u])):
            if u != v:
                tree.append((u, v, G[u][v]))
    return tree

def find_odd_vertexes(MST):
    tmp_g = {}
    vertexes = []
    for edge in MST:
        if edge[0] not in tmp_g:
            tmp_g[edge[0]] = 0
        if edge[1] not in tmp_g:
            tmp_g[edge[1]] = 0
        tmp_g[edge[0]] += 1
        tmp_g[edge[1]] += 1

    for vertex in tmp_g:
        if tmp_g[vertex] % 2 == 1:
            vertexes.append(vertex)

    return vertexes

def minimum_weight_matching(MST, G, odd_vert):
    import random
    random.shuffle(odd_vert)

    while odd_vert:
        v = odd_vert.pop()
        length = float("inf")
        u = 1
        closest = 0
        for u in odd_vert:
            if v != u and G[v][u] < length:
                length = G[v][u]
                closest = u

        MST.append((v, closest, length))
        odd_vert.remove(closest)

def find_eulerian_tour(MatchedMSTree, G):
    neighbours = {}
    for edge in MatchedMSTree:
        if edge[0] not in neighbours:
            neighbours[edge[0]] = []
        if edge[1] not in neighbours:
            neighbours[edge[1]] = []

        neighbours[edge[0]].append(edge[1])
        neighbours[edge[1]].append(edge[0])

    start_vertex = MatchedMSTree[0][0]
    EP = [neighbours[start_vertex][0]]

    while len(MatchedMSTree) > 0:
        for i, v in enumerate(EP):
            if len(neighbours[v]) > 0:
                break

        while len(neighbours[v]) > 0:
            w = neighbours[v][0]
            remove_edge_from_matchedMST(MatchedMSTree, v, w)
            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]
            i += 1
            EP.insert(i, w)
            v = w

    return EP

def remove_edge_from_matchedMST(MatchedMST, v1, v2):
    for i, item in enumerate(MatchedMST):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return MatchedMST

# Criar a janela principal
root = tk.Tk()
root.title("Leitor de Arquivos")

# Criar um botão para abrir o navegador de arquivos
botao_abrir = tk.Button(root, text="Abrir arquivo", command=ler_arquivo)
botao_abrir.pack()

# Loop principal da interface gráfica
root.mainloop()
