import sys
from collections import deque

def main():

    data = sys.stdin.buffer.read().split()

    p = 0

    nodes, edges = int(data[p]), int(data[p+1]); p+=2

    adj = [[] for _ in range(nodes+1)]

    temp = iter(map(int, data[p:p+edges*2])); p+=edges*2

    for u,v in zip(temp, temp):
        adj[v].append(u)
        adj[u].append(v)

    s = 1
    dist = [-1] * (nodes+1)
    dist[s] = 0
    q = deque([s])

    while q:
        u = q.popleft()
        print(u)
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    print(dist)

main()