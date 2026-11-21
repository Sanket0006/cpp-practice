from sys import stdin, stdout

def main():
    data = stdin.buffer.read().split()
    out = []
    p = 0

    t = int(data[p]); p+=1

    for _ in range(t):
        n, q, g = int(data[p]), int(data[p+1]), int(data[p+2]); p+= 3
        # n is number of people
        # q is number of queries, 
        # g is number of genres
        test = []

        for _ in range(q):
            if data[p].decode() is 'P':
                test.append()
            else:

                ...


    stdout.write("\n".join(map(str, out)) + '\n')

main()
