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
        distMin = 0
        distMax = [-1] * (nodes)
        q = deque()

        for u,v in zip(temp,temp):
            adj[u].append(v)
            adj[v].append(u)

        

        for x in range(nodes):
            dist = [-1]*(nodes)
            dist[x] = 0 
            q.append(x)

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            distMax[x] = max(dist)

        s = distMax.index(min(distMax)) #index value not actual value

        dist = [-1] * nodes; dist[s] = 0
        q.append(s)

        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

        maxVal = 1
        for x in dist:
            if x > 0:
                maxVal = max(maxVal, x)  

        out.append(maxVal)          

    sys.stdout.write("\n".join(map(str, out)) + '\n')






main()