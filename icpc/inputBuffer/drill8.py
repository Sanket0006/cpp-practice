# 6
# 1 5
# 2 1 1
# 1 9
# 1 3
# 2 2 3
# 2 1 3
import sys

def main():
    data = sys.stdin.buffer.read().split()
    out = []

    arr = []
    queries = []
    p = 0
    q = int(data[p]); p+=1

    for _ in range(q):
        check = int(data[p])
        if check == 1:
            arr.append(int(data[p+1])); p+=2
        else:
            queries.append([int(data[p+1]), int(data[p+2])]); p+= 3

        
    print(arr, queries, sep='\n')

    sys.stdout.write("\n".join(map(str, out)) + '\n')

main()