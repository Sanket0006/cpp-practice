import sys

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    storage = []
    n,m = int(data[0]),int(data[1]); p = 2

    for i in range(n):
        # storage.append(list(map(str, data[p+i*m: p+(i+1)*m]))); p += m
        storage = [data[p+j].decode() for j in range(n)]

    print(storage)
    sys.stdout.write('\n'.join(map(str, out)) + '\n')
main()