import sys
from collections import deque

def main():
    # data = sys.stdin.buffer.read().split()
    out = []
    p = 0

    # n, e = int(data[p]), int(data[p+1]); p+=2
    # n = num nodes, e = num edges

    n = e = 5
    edges = [[1,2],[1,3],[2,3],[3,4],[4,5]]

    adj = [[] for _ in range(n+1)]
    # [[],[],[],[],[],[]]

    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * (n+1)
    q = deque()
    s = 5
    dist[s] = 0

    q.append(s)

    while q:
        u = q.popleft()

        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    print(dist)


    # q.popleft() removes from front
    # q.append() to add at last
    
    # sys.stdout.write("\n".join(map(str, out))+'\n')

main()