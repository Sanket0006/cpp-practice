def main():

    n = int(input())
    l = []
    s = "{}"

    for i in range(n):
        temp = f"{{{','.join(l)}}}"
        
        l.append(temp)

    print(f"{{{','.join(l)}}}")



    # print(createAnswer(s, l, 0, n))






# def createAnswer(s, l, i, n):
#     if i == n:
#         l.append("{}")
#         return l

#     else:
        
#         return f""




main()