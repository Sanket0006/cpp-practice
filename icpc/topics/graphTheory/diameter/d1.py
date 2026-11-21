from collections import deque
import sys

def main():
    # n nodes, n-1 edges
    q = deque()

    data = sys.stdin.buffer.read().split()
    p = 0
    n = int(data[p]); p += 1

    temp = iter(map(int, data[p: p+(n-1)*2])); p+= (n-1)*2

    adj = [[] for _ in range(n)]

    for u,v in zip(temp, temp):
        adj[u].append(v)
        adj[v].append(u)

    def bfs(k: int):
        dist = [-1] * n
        parent = [-1] * n
        dist[k] = 0
        q.append(k)
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
        return dist, parent


    
    d1, _ = bfs(0)
    print(d1)

    d2, p2 = bfs(d1.index(max(d1)))

    c = d2.index(max(d2))
    D = d2[c]

    x = c
    for _ in range(D // 2):
        x = p2[x]

    print(x)

    d3, _ = bfs(x)

    print(max(d3))


main()