import heapq


def dijkstra(adj, src, destinations=None):
    V = len(adj) - 1

    dist = [float("inf")] * (V + 1)
    dist[src] = 0

    parent = [None] * (V + 1)
    S = [False] * (V + 1)
    Q = [(0, src)]

    while Q:
        d, u = heapq.heappop(Q)

        if d > dist[u] or S[u]:
            continue

        S[u] = True

        if destinations is not None:
            if all(S[x] for x in destinations):
                break

        for v, w in adj[u]:
            if not S[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(Q, (dist[v], v))

    return dist, parent


def extract_path(parent, src, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == src:
            break

        current = parent[current]

    if path[-1] != src:
        return []

    path.reverse()
    return path


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
    destinations = [6, 8, 9, 15, 16, 22]

    dist, parent = dijkstra(adj, src, destinations)

    print(f"Shortest paths from Node {src}")

    for destination in destinations:
        path = extract_path(parent, src, destination)

        if not path:
            print(f"Node {destination}: Unreachable")
        else:
            path_string = " -> ".join(map(str, path))
            print(f"Node {destination}:")
            print(f"\tDistance: {dist[destination]}")
            print(f"\tPath: {path_string}")


if __name__ == "__main__":
    main()
