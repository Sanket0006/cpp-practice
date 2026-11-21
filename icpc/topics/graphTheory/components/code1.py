import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    n, e = int(data[p]), int(data[p+1]); p+=2
    out = []

    temp = iter(map(int, data[p:p+e*2])); p+=e*2
    adj = [[] for _ in range(n)]

    for u,v in zip(temp, temp):
        adj[u].append(v)
        adj[v].append(u)
    ans = 0
    dist = [-1]*n
    s = 0


    for i in range(n):
        if dist[i] == -1:
            dist[i] = 0
            ans += 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v) 

    # for i,x in enumerate(dist):
    #     if x != -1:
    #         out.append(i)

    # sys.stdout.write(" ".join(map(str, out)) + '\n')
    print(ans)

main()