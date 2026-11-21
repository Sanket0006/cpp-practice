def main():

    nums = [0,0,1]


    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1

    # -1 -1 1
    # -1 -2 -1

    psum = [0]*len(nums)
    print(psum)
    psum[0] = nums[0]
    print(psum)


    hashmap = {0:-1, psum[0]:0}
    best_len = 0
    
    for i in range(1, len(nums)):
        psum[i] = nums[i]+psum[i-1]
        if psum[i] not in hashmap:
            hashmap[psum[i]] = i
        else:
            best_len = max(best_len, i - hashmap[psum[i]])

    print(psum, hashmap, best_len)


main()