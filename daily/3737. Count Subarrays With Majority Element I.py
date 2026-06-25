from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 1
        freq = [0] * (2 * n + 3)

        prefix = 0

        less = 0

        answer = 0

        freq[offset] = 1

        for value in nums:
            if value == target:
                less += freq[prefix + offset]
                prefix += 1
            else:
                prefix -= 1

                less -= freq[prefix + offset]

            answer += less

            freq[prefix + offset] += 1

        return answer