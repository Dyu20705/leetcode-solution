class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        res = [0] * len(nums)
        for num, indices in d.items():
            n = len(indices)
            if n == 1:
                continue

            prefix_sum = [0] * n
            prefix_sum[0] = indices[0]
            for i in range(1, n):
                prefix_sum[i] = prefix_sum[i - 1] + indices[i]

            for i, index in enumerate(indices):
                left_sum = index * i - (prefix_sum[i - 1] if i > 0 else 0)
                right_sum = (prefix_sum[-1] - prefix_sum[i]) - index * (n - 1 - i)
                res[index] = left_sum + right_sum

        return res