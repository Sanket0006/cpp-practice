from collections import deque
import sys

def main():
    f,s,g,u,d = input().split()
    f,s,g,u,d = int(f), int(s), int(g), int(u), int(d)

    dist = [-1] * (f+1)

    dist[s] = 0
    q = deque([s])

    while q:
        x = q.popleft()

        for v in (x+u,x-d):
            if 1<=v<=f and dist[v] == -1:
                dist[v] = dist[x] + 1
                q.append(v)


    print(dist[g]) if dist[g] != -1 else print("use the stairs")


main()