from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)

        ones = freq.pop(1, 0)

        ans = ones if ones & 1 else ones - 1
        if ans < 1:
            ans = 1

        get = freq.get

        LIMIT = 31_622

        for x, count in freq.items():
            if count < 2 or x > LIMIT:
                continue

            y = x * x

            if get(y, 0) == 0:
                continue

            length = 3

            while y <= LIMIT and get(y, 0) > 1:
                y *= y

                if get(y, 0) == 0:
                    break

                length += 2

            if length > ans:
                ans = length

        return ans