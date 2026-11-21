import sys

def main():
    data = sys.stdin.buffer.read().split()

    out = list(map(int, data[:]))

    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()