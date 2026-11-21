def main():

    p,n,d,t = input().split()
    p = int(p)
    n = int(n)
    d = int(d)
    t = int(t)

    if (d%p == 0):
        if (d == 0):
            print("no")
        elif ((p*n)/d >= t):
            print("no")
        else:
            print("yes")
    else:
        print("yes")


main()