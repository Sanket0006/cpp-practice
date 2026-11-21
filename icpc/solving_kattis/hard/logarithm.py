import sys, math

def main():

    data = sys.stdin.buffer.read().split()

    d = list(map(int, data))

    out = []

    for num in d:
        fac = 0


        for i in range(1, num+1):
            fac += math.log10(i)

        if (num == 0 or num == 1):
            fac = 1

        out.append(math.ceil(fac))
        
    sys.stdout.write("\n".join(map(str, out)) + '\n')

main()