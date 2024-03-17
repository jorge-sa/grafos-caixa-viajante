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
    print(f'Este grafo possui {n-1} cidades')
    start_city = int(input("Cidade inicial: "))
    end_city = int(input("Cidade de destino: "))
    distances = dijkstra(graph, start_city)
    shortest_distance = distances[end_city]
    
    # Reconstruction of the shortest path
    path = [end_city]
    current_city = end_city
    while current_city != start_city:
        for city, dist in enumerate(graph[current_city]):
            if dist > 0 and distances[current_city] - dist == distances[city]:
                path.append(city)
                current_city = city
                break
    path.reverse()

    print("A distância mais curta da cidade", start_city, "para a cidade", end_city, "é:", shortest_distance)
    print("O caminho mais curto é:", path)

if __name__ == "__main__":
    main()
