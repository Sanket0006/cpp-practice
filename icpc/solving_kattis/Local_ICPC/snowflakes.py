import sys
from collections import defaultdict

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    p = 0
    t = int(data[p]); p+=1

    for _ in range(t):
        n = int(data[p]); p+=1
        arr = list(map(int, data[p:p+n])); p+=n
        best = 1
        hmap = defaultdict(int)
        left = 0

        # we keep track of left window, if the element in hashmap,
        # we move left to element's index + 1 (only if hmap's current element's index is greater than left) 



        for i,x in enumerate(arr):
            if x in hmap:
                # Why if statement? because what if two elements are similar 1,2,2,3,4 then it will stuck at 2
                # so instead we move until we d
                if hmap[x] >= left:
                    left = hmap[x] + 1
            best = max(best, i-left+1)
            hmap[x] = i
        
        out.append(max(best, i-left+1))

    sys.stdout.write("\n".join(map(str, out)) + '\n')

main()



