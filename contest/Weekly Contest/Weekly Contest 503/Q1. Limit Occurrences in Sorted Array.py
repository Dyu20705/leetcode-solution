class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        result = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
            if count[num] <= k:
                result.append(num)
        return result