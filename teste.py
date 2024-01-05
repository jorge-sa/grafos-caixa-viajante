import sys

class City:
    def __init__(self):
        self.visitado = False
        self.vizinhos = []
        
    def def_neig_dist(self,lista_city:list,lista_dist:list):
        self.vizinhos = [(x,int(z)) for x,z in zip(lista_city,lista_dist)]
        print(self.vizinhos)

def vizinho_nao_visitado_distancia(x:tuple):
    if x[0].visitado or x[1] == 0:
        return sys.maxsize
    
    return x[1]

def distancia_retorno_inicio(x:City, inicio:City):
    return [y[1] for y in x.vizinhos if y[0]==inicio]

#tabela de distancia entre vertices
#-------definir matriz de distancia

lista_city = []
for x in range(len(matrix_dist)):
    lista_city.append(City())

for x,y in zip(lista_city,matrix_dist):
    x.def_neig_dist(lista_city, y)

inicio = lista_city[0]
cur = inicio
cur.visitado = True
dist = 0
while not all([x.visitado for x in lista_city]):
    tar = min(cur.vizinhos, key=vizinho_nao_visitado_distancia)
    dist += tar[1]
    cur = tar[0]
    cur.visitado = True
    print(cur)


print(dist + sum(distancia_retorno_inicio(cur,inicio)))