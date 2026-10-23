import heapq


def dijkstra(adj, src):
    V = len(adj) - 1

    dist = [float("inf")] * (V + 1)
    dist[src] = 0

    Q = [(0, src)]

    while Q:
        d, u = heapq.heappop(Q)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))

    return dist


def main():
    V = 22
    adj = [[] for _ in range(V + 1)]

    edges = [
        (1, 2, 1),
        (1, 11, 1),
        (2, 3, 1),
        (2, 21, 1),
        (3, 4, 1),
        (3, 8, 2),
        (4, 5, 1),
        (5, 22, 1),
        (5, 7, 1),
        (5, 6, 2),
        (6, 7, 2),
        (7, 8, 1),
        (8, 9, 2),
        (9, 10, 1),
        (9, 19, 2),
        (10, 11, 1),
        (10, 18, 2),
        (11, 12, 2),
        (11, 17, 1),
        (12, 13, 2),
        (13, 14, 2),
        (13, 21, 1),
        (14, 15, 1),
        (14, 16, 1),
        (14, 20, 1),
        (16, 17, 2),
        # (17, 18, 2),
        (18, 19, 2),
        (20, 21, 2),
        (20, 22, 1),
        # (21, 22, 2)
    ]

    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    src = 1
    dist = dijkstra(adj, src)

    print(f"Shortest distances from Node {src}")

    for node in range(1, V + 1):
        if dist[node] == float("inf"):
            print(f"Node {node}: Unreachable")
        else:
            print(f"Node {node}: Distance = {dist[node]}")


if __name__ == "__main__":
    main()
