import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matrix_builder

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

#gerar matriz
mtx = matrix_builder.build_graph_matrix()

edges = formEdges(mtx)
edges.sort(key=lambda x: x.w)

v = []
arestas = []
while True:
    for e in edges:
        if (e.vtx[1] not in v or e.vtx[0] not in v):
            arestas.append(e)
            v.append(e.vtx[0])
            v.append(e.vtx[1])
        if set(v) == {0,1,2,3,4}:
            break
    break 
    
#ver arestas selecionadas
for a in arestas:
    print(a.vtx,a.w)