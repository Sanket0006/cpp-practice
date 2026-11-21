import sys
from collections import deque

def main():

    data = sys.stdin.buffer.read().split()
    out = []
    p = 0
    nodes, edges = int(data[p]), int(data[p+1]); p+=2

    adj = [[] for _ in range(nodes + 1)]

    temp = iter(map(int, data[p:p+edges*2])); p+=edges*2

    for u,v in zip(temp, temp):
        adj[u].append(v)
        adj[v].append(u)

    s = int(data[p]); p+=1

    dist = [-1]*(nodes+1)
    dist[s] = 0
    q = deque([s])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    for i, x in enumerate(dist[1:], 1):
        out.append(f"{i}: {x}")

    sys.stdout.write("\n".join(map(str, out)) + '\n')



main()