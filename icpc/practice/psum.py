def main():

    arr = [1,2,3,4,5]

    psum = [0]

    for i in range(len(arr)):
        psum.append(arr[i]+psum[-1])

    

    print(arr,psum, sep='\n')

    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i-1]

    print(arr)

main()