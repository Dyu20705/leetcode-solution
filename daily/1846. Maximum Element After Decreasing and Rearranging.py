from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(
        self, arr: List[int]
    ) -> int:
        n = len(arr)
        count = [0] * (n + 1)

        for x in arr:
            count[x if x <= n else n] += 1

        maximum = 0

        for value in range(1, n + 1):
            maximum += count[value]

            if maximum > value:
                maximum = value

        return maximum