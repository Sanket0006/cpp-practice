import sys

def main():
    data = sys.stdin.buffer.read().split()
    inp = data[1:]

    for i in range(len(inp)):
        inp[i] = inp[i].decode()

    stackLeft = []
    stackRight = []

# 🧦 🧦 🧦 👟 🧦 👟


    for emoji in inp:
        if emoji == '🧦':
            if (len(stackLeft) == len(stackRight) == 2):
                return "ógilt"

            elif (len(stackLeft)==2 and len(stackRight)==1):
                stackRight.pop()
                
            elif len(stackLeft)==1 and len(stackRight)==1:
                stackLeft.pop()

            elif len(stackLeft) in [1,2] and len(stackRight) == 0:
                stackRight.append(emoji)

            elif len(stackLeft) == 0 and len(stackRight) == 2:
                stackLeft.append(emoji)

            else:
                stackLeft.append(emoji)
        else:
            if ((len(stackLeft) in [0,2]) and len(stackRight) == 0) or (len(stackLeft) == 2 and len(stackRight) == 2):
                return "ógilt"

            elif len(stackLeft) in [0,2] and len(stackRight) == 1:
                stackRight.append(emoji)

            elif len(stackLeft) == 1 and len(stackRight) in [0,1,2]:
                stackLeft.append(emoji)


            else:
                return "ógilt"

    if len(stackRight) == len(stackLeft) == 2:
        return 'gilt'
    else:
        return "ógilt"


    


print(main())