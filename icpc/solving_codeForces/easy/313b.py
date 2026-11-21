import sys

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    p = 0
    string = data[p].decode(); p+=1

    q = int(data[p]); p+=1 
    queries = []

    for _ in range(q):
        queries.append([int(data[p]), int(data[p+1])]); p+=2

    string = " "+string

    psum = []

    for i in range(len(string)-1):
        psum.append(1 if string[i] == string[i+1] else 0)

    for i in range(1, len(psum)):
        psum[i] = psum[i] + psum[i-1]

    for l,r in queries:
        out.append(psum[r-1] - psum[l-1])


    sys.stdout.write("\n".join(map(str,out)) + '\n')


main()