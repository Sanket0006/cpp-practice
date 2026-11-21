from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        q = deque([0])

        dct = defaultdict(list)

        for i,x in enumerate(arr):
            dct[x].append(i)



        def bfs():
            dist = [-1]*len(arr)
            dist[0] = 0

            while q:
                u = q.popleft()

                for v in (u-1, u+1):
                    if 0<=v<len(arr) and dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)

                for v in dct[arr[u]]:
                    if 0<=v<len(arr) and dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
                dct[arr[u]].clear()
            return dist

        dist = bfs()

        return dist[-1]        