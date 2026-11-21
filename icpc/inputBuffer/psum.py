# prefix sum problem
import sys

def main():
    data = sys.stdin.buffer.read().split()
    out = []

    n = int(data[0]) # size of array
    arr = list(map(int, data[1:1+n])) # array, idx 1, n (n+1 in non inclusive)
    q_num = int(data[n+1]) # number of queries

    it = iter(map(int, data[n+2:n+2+q_num*2])) 

    psum = [0]

    for x in arr:
        psum.append(x + psum[-1])

    for l,r in zip(it, it):
        out.append(psum[r] - (psum[l-1]))

    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()
