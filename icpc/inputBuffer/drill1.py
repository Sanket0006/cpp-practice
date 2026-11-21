import sys

def main():
    data = sys.stdin.buffer.read().split()
    out = []

    n = int(data[0])
    arr = list(map(int, data[1:1+n]))

    out = arr
    sys.stdout.write('\n'.join(map(str, arr)) + '\n')

main()