import heapq


class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight


def dijkstra(adj, src, destinations=None):
    # Number of vertices (index 0 is unused)
    V = len(adj) - 1

    # INITIALIZE-SINGLE-SOURCE(G, s)
    dist = [float("inf")] * (V + 1)
    dist[src] = 0

    # Parent of each vertex in the shortest-path tree
    parent = [None] * (V + 1)

    # S: vertices whose shortest distances are finalized
    S = [False] * (V + 1)

    # Q: min-priority queue storing (distance, vertex)
    Q = []
    heapq.heappush(Q, (0, src))

    while Q:
        # EXTRACT-MIN(Q)
        d, u = heapq.heappop(Q)

        # Skip outdated entries or already settled vertices
        if d > dist[u] or S[u]:
            continue

        # Finalize u
        S[u] = True

        # Stop when all required destinations are finalized
        if destinations is not None:
            if all(S[destination] for destination in destinations):
                break

        # Relax edges
        for edge in adj[u]:
            v = edge.node
            w = edge.weight

            if not S[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u  # Record predecessor of v
                heapq.heappush(Q, (dist[v], v))

    return dist, parent


def extract_path(parent, src, destination):
    # Follow parent pointers backward from destination
    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == src:
            break

        current = parent[current]

    # If we did not reach the source, no path was found
    if path[-1] != src:
        return []

    # Reverse to get the path from source to destination
    path.reverse()
    return path


def main():
    V = 22

    # Create a 1-indexed adjacency list
    adj = [[] for _ in range(V + 1)]

    # Weighted undirected edges: (u, v, weight)
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

    # Build the undirected graph
    for u, v, w in edges:
        adj[u].append(Edge(v, w))
        adj[v].append(Edge(u, w))

    src = 1
    destinations = [6, 8, 9, 15, 16, 22]

    # Run Dijkstra
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
