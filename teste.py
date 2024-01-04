class City:
    def __init__(self):
        self.visitado = False
        self.vizinhos = []
        
    def def_neig_dist(self,lista_city:list,lista_dist:list):
        self.vizinhos = [(x,int(z)) for x,z in zip(lista_city,lista_dist)]
        print(self.vizinhos)

lista_dist = [
[0.0 , 3.0 , 4.0 , 2.0 , 7.0],
[3.0 , 0.0 , 4.0 , 6.0 , 3.0],
[4.0 , 4.0 , 0.0 , 5.0 , 8.0],
[2.0 , 6.0 , 5.0 , 0.0 , 6.0],
[7.0 , 3.0 , 8.0 , 6.0 , 0.0]
]
lista_city = []
for x in range(len(lista_dist)):
    lista_city.append(City())

for x,y in zip(lista_city,lista_dist):
    x.def_neig_dist(lista_city, y)