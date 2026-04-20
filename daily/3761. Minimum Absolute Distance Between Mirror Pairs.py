class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        ans = float('inf')
        for i, n in enumerate(nums):
            if n in hashmap:
                ans = min(ans, i - hashmap[n])
            hashmap[int(str(n)[::-1])] = i
        return ans if ans != float('inf') else -1
