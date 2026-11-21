import sys


data = sys.stdin.buffer.read().decode()

for _ in data:
    if _ == '\n\n':
        print("LINE")

print(data)