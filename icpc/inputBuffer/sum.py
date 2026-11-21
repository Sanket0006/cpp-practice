# this file directory is to learn about taking input in one line.

import sys

class solution:
    def main() -> int:
        data = sys.stdin.buffer.read().split()

        n = int(data[0])
        p = list(map(int, data[1:1+n]))

        print(sum(p))

    if __name__ == "__main__":
        main()