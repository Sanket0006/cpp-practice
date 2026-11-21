def main():

    l = [[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]

    arr = l[0][0]

    print(arr)
    
    # for r1,c1,r2,c2 in l[1:]:
    #     print(r1,c1,r2,c2)

    for i in range(len(arr)):
        for j in range(len(arr[i])-1):
            arr[i][j+1] = arr[i][j+1] + arr[i][j]

    for i in range(len(arr)-1):
        for j in range(len(arr[i])):
            arr[i+1][j] = arr[i+1][j] + arr[i][j]


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')

        print()

    print(solution(arr, 0, 0, 0, 0))
    

     
    

    
def solution(arr: list[list[int]], row1, col1, row2, col2):
    # if (row1 == 0 and col1 == 0): 
    #     return arr[row2][col2]
    
    arr1 = arr[row1-1][col2] if row1>0 else 0
    arr2 = arr[row2][col1-1] if col1>0 else 0
    arr3 = arr[row1-1][col1-1] if row1>0 and col1>0 else 0

    return arr[row2][col2] - arr1 - arr2 + arr3

    print(arr[row2][col2], arr[max(row1 - 1,0)][col2], arr[row2][max(col1-1, 0)], arr[max(row1-1, 0)][max(col1-1, 0)])

main()