from collections import defaultdict


def subarraySum(nums: list[int], k: int) -> int:
    occ = defaultdict(int)
    occ[0]+=1
    ans = 0
    psum = [0]

    for i in range(len(nums)):
        temp = nums[i]+psum[-1]
        
        psum.append(temp)
        occ[temp] += 1
        
        if temp-k in occ:
            ans += occ[temp-k]
    print(ans)

def main():
    subarraySum([1,1,1],2)

main()