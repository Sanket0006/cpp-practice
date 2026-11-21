from collections import deque
from time import sleep

class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        q = deque()

        adj = [[] for _ in range(n+1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist1 = [-1] * (n+1)
        dist2 = [-1] * (n+1)
        q.append((1,0))
        dist1[1] = 0
        while q:
            u, d = q.popleft()
            for v in adj[u]:
                if dist1[v] == -1:
                    dist1[v] = d + 1
                    q.append((v, dist1[v]))
                elif dist2[v] == -1 and d+1 > dist1[v]:
                    dist2[v] = d + 1
                    q.append((v, dist2[v]))



        dst = dist2[-1]
        red = False
        t = 0
        i = 0

        print(dist1, dist2)
        while True:
            if (t % (change*2) >= change):
                if not red:
                    red = True
            else:
                red = False
            
            if i == dst:
                break
            elif red:
                t+=1
            else:
                t+=time
                i+=1        
            
        return t




ob = Solution()
print(ob.secondMinimum(5,[[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))
