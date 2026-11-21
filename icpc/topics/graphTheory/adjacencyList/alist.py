import sys

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    p = 0

    nodes, edges = int(data[p]), int(data[p+1]); p+=2

    adj = [[] for _ in range(nodes+1)]

    inp = iter(map(int, data[p:p+edges*2]))
    for u, v in zip(inp, inp):
        adj[u].append(v)
        adj[v].append(u)


    for i, cur in enumerate(adj[1:],1):
        temp = " ".join(map(str, cur))
        out.append(f"{i}: {len(cur)} -> {temp}")
    
    sys.stdout.write("\n".join(map(str, out))+'\n')

main()