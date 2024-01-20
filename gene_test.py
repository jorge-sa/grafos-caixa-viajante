import matrix_builder
import random

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

def fitness():
    pass

def selection():
    pass
    
def procreate():
    pass

def mutation():
    pass