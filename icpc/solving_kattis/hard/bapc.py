def main():

    l1 = input(); n,m,r = l1.split()

    n = int(n); m = int(m); rank = int(r)

    pending = 0

    before = 0
    fav_pending = 0
    after = 0
    
    for i in range(n):
        temp = input()

        if i == rank-1:
            for c in temp:
                if c == 'P':
                    fav_pending += 1
                    pending +=1

        elif i < rank-1:
            for c in temp:
                if c == 'P':
                    before+=1
                    pending+=1

        else:
            for c in temp:
                if c == "P":
                    pending+=1
                    after += 1
        

    for i in range(pending):
        temp = input()

        if (before < i <= before+fav_pending):
            if temp.startswith("Ooohhh... Aaayyy"):
                rank -= len(temp[15:])-4



    print(rank)

main()