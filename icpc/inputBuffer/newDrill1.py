import sys

def main():
    data = sys.stdin.buffer.read().split()

    out = list(map(int, data))
    out.pop() #removing last zero

    sys.stdout.write("\n".join(map(str, out)) + '\n')

main()