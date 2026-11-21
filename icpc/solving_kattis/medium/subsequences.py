from collections import defaultdict
import sys

def subarraySum(nums: list[int], k: int) -> int:
    occ = defaultdict(int)
    occ[0]+=1
    ans = 0
    psum = [0]

    for i in range(len(nums)):
        temp = nums[i]+psum[-1]
        
        
        if temp-k in occ:
            ans += occ[temp-k]

        psum.append(temp)
        occ[temp] += 1
    return ans

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    out = []
    t = int(data[p]); p+=1

    for i in range(t):
        n = int(data[p]); p+=1
        arr = list(map(int, data[p:p+n])); p+=n

        out.append(subarraySum(arr, 47))

    sys.stdout.write("\n".join(map(str, out)) + '\n')



main()