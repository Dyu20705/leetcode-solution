from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        freq = [0] * (2 * n + 1)

        idx = n
        freq[idx] = 1

        less = 0
        answer = 0

        for value in nums:
            if value == target:
                less += freq[idx]
                idx += 1
            else:
                idx -= 1
                less -= freq[idx]

            answer += less
            freq[idx] += 1

        return answer