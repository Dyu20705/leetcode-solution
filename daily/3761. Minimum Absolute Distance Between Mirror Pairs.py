class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mirror_pairs = {}
        for i, num in enumerate(nums):
            if num not in mirror_pairs:
                mirror_pairs[num] = [i]
            else:
                mirror_pairs[num].append(i)

        min_distance = float('inf')
        for indices in mirror_pairs.values():
            if len(indices) >= 2:
                for j in range(1, len(indices)):
                    distance = indices[j] - indices[j - 1]
                    min_distance = min(min_distance, distance)

        return min_distance if min_distance != float('inf') else -1

        # a = []
        # l = len(nums)
        # for i in range(0,l):
        #     for j in range(i+1, l):
        #         if nums[i] == int(str(nums[j])[::-1]):
        #             a.append(abs(i - j))
        # return min(a) if a else -1