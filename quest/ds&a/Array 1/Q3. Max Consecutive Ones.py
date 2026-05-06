class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        result = []
        for a in nums:
            if a == 1:
                i+=1
            elif a == 0:
                result.append(i)
                i =0
        result.append(i)
        return max(result)
            
        