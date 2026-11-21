from collections import deque
import sys

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    t = int(data[p]); p+=1
    out = []
    
    for _ in range(t):
        nodes = int(data[p]); p+=1

        temp = iter(map(int, data[p:p+(nodes-1)*2])); p+=(nodes-1)*2

        adj = [[] for y in range(nodes)]
        q = deque()

        for u,v in zip(temp,temp):
            adj[u].append(v)
            adj[v].append(u)

        def bfs(k: int):
            q.append(k)
            dist = [-1] * nodes
            parent = [-1] * nodes
            dist[k] = 0

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
            return dist, parent

        d1, _ = bfs(0)

        d2, p2 = bfs(d1.index(max(d1)))
        # print(d2)

        c = d2.index(max(d2))
        # D = d2[c]
        distt = d2[c]
        # print(distt)

        # x = c
        # for _ in range(D//2):
        #     x = p2[x]

        # d3, _ = bfs(x)

        # out.append(max(d3))
        out.append(distt//2 if distt % 2 == 0 else distt//2 + 1)

    sys.stdout.write("\n".join(map(str, out)) + '\n')

main()