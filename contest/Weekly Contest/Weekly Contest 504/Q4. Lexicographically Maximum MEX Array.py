class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        N = len(nums)
        M = max(max(nums), N) + 2
        
        seen = [0] * M
        suffix = [0] * N
        mex = 0
        
        for i in range(N-1, -1, -1):
            seen[nums[i]] = 1
            while seen[mex]:
                mex += 1
            suffix[i] = mex
    
        ans = []
        seen = [-1] * M
        i = 0
        seg = 0
        
        while i < N:
            mex = suffix[i]
            if mex == 0:
                ans.append(0)
                i += 1
            else:
                cnt, j = 0, i
                while True:
                    x = nums[j]
                    if x < mex and seen[x] != seg:
                        seen[x] = seg
                        cnt += 1
                        
                        if cnt == mex:
                            break
                            
                    j += 1
                    
                ans.append(mex)
                i = j+1
                
            seg += 1
            
        return ans