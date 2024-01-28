import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matrix_builder
import random

#calcular distancia percorrida
def calc_dist(sub:list):
    d = 0                           #distância percorrida
    for i in range(0,len(sub)-1):
        val = mtx[sub[i]-1][sub[i+1]-1]
        d += val
    else:
        d += mtx[sub[-1]-1][sub[0]-1]
    
    return d

def fitness():
    pass

def selection():
    pass
    
def procreate():
    pass

def mutation():
    pass

#gerar matriz
mtx = matrix_builder.build_graph_matrix()

#define população inicial
pop_size = int(input("set pop size: "))
pop = list()
for n in range(pop_size):
    subject = [1]
    while len(subject) != len(mtx):
        m = random.randint(2, len(mtx))
        if m not in subject:
            subject.append(m)
    pop.append(subject)

for line in mtx:
    print(line)

print(pop)

for elem in pop:
    print(f"final: {calc_dist(elem)}")