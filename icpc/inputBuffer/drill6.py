import sys

def main():
    data = sys.stdin.buffer.read().split()
    storage = []
    out = []
    p = 0

    n = int(data[p]); p += 1

    for _ in range(n):
        storage.append([data[p].decode(), int(data[p+1])]); p += 2
        

    print(storage)

    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()