import sys

def main():
    data = sys.stdin.buffer.read().split()

    n = int(data[0]) # len of array , idx 0
    arr = list(map(int, data[1:1+n])) # array, idx 1 to n+1 (n+1 is non inclusive)
    q = int(data[1+n]) # number of queries, idx n+1
    queries = list(map(int, data[n+2:n+q+2]))

    out = []

    for i in queries:
        out.append(arr[i-1])

    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()