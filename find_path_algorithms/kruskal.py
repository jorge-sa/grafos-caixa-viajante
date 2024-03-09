import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matrix_builder

#gerar matriz
mtx = matrix_builder.build_graph_matrix()

class edge():
    def __init__(self, v1, v2, w) -> None:
        self.vtx = (v1,v2)
        self.w = w

#calcular distancia percorrida
def calc_dist(sub:list):
    d = 0                                                   #distância percorrida
    for i in range(0,len(sub)-1):
        val = mtx[sub[i]-1][sub[i+1]-1]
        d += val
    else:
        d += mtx[sub[-1]-1][sub[0]-1]
    
    return d

def formEdges(matrix:list):
    edges = list()

    for i in range(1, len(matrix)):
        for j in range(i):
            edges.append(edge(i,j,matrix[i][j]))

    return edges

def isCycleUtil(graph, vertx, parent, visited):
    print(vertx, parent, visited)
    if vertx in visited:
        return False
    
    visited.add(vertx)

    for childV in graph[vertx]:
        print(childV)
        if childV in visited and childV != parent:
            print("já visitado", childV)
            return True
        
        if isCycleUtil(graph, childV, vertx, visited):
            return True
    else:
        return False

def isCycle(v:list, graph:list):
    adj = {}

    for ve in v:
        adj[ve] = []
        for e in graph:
            if ve in e.vtx:
                adj[ve].append(e.vtx[0] if e.vtx[0] != ve else e.vtx[1])

    start = list(adj.keys())[0]
    visited = set()
    if isCycleUtil(adj, start, -1, visited):
        print("Found cycle")
        return True
    
    print("no cycle")
    return False

edges = formEdges(mtx)
edges.sort(key=lambda x: x.w)

v = []
arestas = []
i = 0
while len(arestas) < len(mtx)-1:
    e = edges[i]
    if (e.vtx[1] not in v or e.vtx[0] not in v):
        arestas.append(e)
        v.append(e.vtx[0])
        v.append(e.vtx[1])
    else:
        print("pontos já encontrados")
        if not isCycle(v, arestas+[e]):
            print("a added")
            arestas.append(e)

    i += 1
    
#ver arestas selecionadas
print("============================")
print("Arestas selecionadas:")
for a in arestas:
    print(a.vtx,a.w)

print("============================")
print("Tamanho do grafo:", len(mtx))
print("N° de arestas:", len(arestas))
print("Vértices visitados:", set(v))
print("Peso:", sum([x.w for x in arestas]))
print("============================")