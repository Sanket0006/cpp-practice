def main():

    logs = [[1993,1999],[2000,2010]]

    arr = [0]*101

    for birth, death in logs:
        arr[birth-1950] += 1
        arr[death-1950] -= 1

    for i in range(1, 101):
        arr[i] = arr[i] + arr[i-1]    

    year = 1950 + arr.index(max(arr))

    print(year)

main()