#Uses python3

def distance(adj, a, b):
    #write your code here
    dist = [len(adj)] * len(adj)
    dist[a] = 0
    queue = []
    queue.append(a)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == len(adj):
                queue.append(v)
                dist[v] = dist[u] + 1
    if dist[b] != len(adj):
        return dist[b]
    return -1

    # # show path from t to s in reverse order
    # while t != -1:
    #     print(t + 1, end=' ')  # must add 1 to t since it's 0-based indexing!
    #     t = prev[t]  # reassign t and check condition again (in while)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        # adjacency list
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = map(int, input().split())
    s = s - 1
    t = t - 1
    print(distance(adj, s, t))
