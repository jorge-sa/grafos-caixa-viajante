
import heapq
from matrix_builder import build_graph_matrix
def dijkstra(graph, start):
    n_vertices = len(graph)
    visited = [False] * n_vertices
    distance = [float('inf')] * n_vertices
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        _, u = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        for v in range(n_vertices):
            if not visited[v] and graph[u][v] > 0:
                alt = distance[u] + graph[u][v]
                if alt < distance[v]:
                    distance[v] = alt
                    heapq.heappush(queue, (alt, v))

    return distance

def main():
    graph = build_graph_matrix()
    n = len(graph)
    print(f'Esse grafo possui {n-1} cidades')
    start_city = int(input("Cidade inicial: "))
    distances = dijkstra(graph, start_city)
    print("Distâncias mais curtas entre a cidade", start_city, ":")
    for i, dist in enumerate(distances):
        print("Para a cidade", i, ": ", dist)

if __name__ == "__main__":
    main()
