import sys

def main():
    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    arr = list(map(int, data[1:1+n]))

    for x in arr:
        if x == 1:
            print("HARD")
            break
    else: 
        print("EASY")

main()