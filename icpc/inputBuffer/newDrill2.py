import sys

def main():
    data = sys.stdin.buffer.read().split()

    data = iter(map(int, data))
    out = zip(data,data)
    

    sys.stdout.write("\n".join(map(str, out)) + '\n')
main()