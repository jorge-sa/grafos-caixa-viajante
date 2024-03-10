import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matrix_builder
import itertools

def traveling_salesman(matrix):
    n = len(matrix)
    min_distance = sys.maxsize
    best_route = None
    for route in itertools.permutations(range(n)):
        total_distance = 0
        for i in range(n - 1):
            origin = route[i]
            destination = route[i + 1]
            total_distance += matrix[origin][destination]
        total_distance += matrix[route[-1]][route[0]]
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route
    return best_route, min_distance

distance_matrix = matrix_builder.build_graph_matrix()

best_route, min_distance = traveling_salesman(distance_matrix)
print("Best route:", best_route)
print("Minimum distance:", min_distance)