from collections import deque

class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0 
        n = len(nums)-1

        dist = [-1] * n; dist[0] = 0

        q = deque([0])

        while q:
            u = q.popleft()
            pos = [(u+i) for i in range(nums[u])]
            
            for v in pos:
                if 0<=v<n and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        return dist[-1]

ob = Solution()
print(ob.jump([2,3,1,1,4]))
print(ob.jump([2,3,0,1,4]))
print(ob.jump([0]))
