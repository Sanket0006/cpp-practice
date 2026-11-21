import sys

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    out = None

    n = int(data[p]); p+=1 

    student = 0; visitor = 0; faculty = 0

    for _ in range(n):
        if (data[p].decode() == "STU"):
            if (data[p+1].decode() == "IN"):
                student += int(data[p+2])
            else:
                student -= int(data[p+2])
        elif (data[p].decode() == "FAC"):
            if (data[p+1].decode() == "IN"):
                faculty += int(data[p+2])
            else:
                faculty -= int(data[p+2])
        else:
            if (data[p+1].decode() == "IN"):
                visitor += int(data[p+2])
            else:
                visitor -= int(data[p+2])
        p+=3

    if (student + faculty + visitor):
        print(student + faculty + visitor)
    else:
        print("NO STRAGGLERS")



main()