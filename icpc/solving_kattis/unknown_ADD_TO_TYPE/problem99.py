import sys
import bisect

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    p=0

    n,q = int(data[p]), int(data[p+1]); p+=2

    arr = list(map(int, data[p: p+n])); p+=n

    temp = iter(map(int, data[p: p+q*2])); p+=q*2
    ops = list(zip(temp,temp))


    for t,num in ops:
        i = bisect.bisect_right(arr, num)
        if i == -1:
            out.append(-1)
            break
        # out.append(arr.pop(i))

    print(n,q)
    print(arr)
    print(ops)


main()