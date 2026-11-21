# 3
# 2
# 1 2
# 3
# 4 5 6
# 1
# 9
import sys

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    ptr = 0
    t = int(data[ptr]); ptr += 1

    for _ in range(t):
        count = int(data[ptr]); ptr += 1
        out.append(list(map(int, data[ptr: ptr+count]))); ptr += count

    sys.stdout.write("\n".join(map(str,out)) + '\n')

main()