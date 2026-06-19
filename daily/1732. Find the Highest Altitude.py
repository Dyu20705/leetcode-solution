class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        cur = 0
        for i in gain:
            cur += i
            if cur > max:
                max = cur
        return max