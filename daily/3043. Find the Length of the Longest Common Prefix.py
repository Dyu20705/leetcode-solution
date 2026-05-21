class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        p_set = set()
        for val in arr1:
            while val not in p_set and val > 0:
                p_set.add(val)
                val //= 10
        longest = 0
        for val in arr2:
            while val not in p_set and val > 0:
                val //= 10
            if val in p_set:
                longest = max(longest, len(str(val)))
        return longest