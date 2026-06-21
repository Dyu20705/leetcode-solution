from bisect import bisect_left, bisect_right

class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        total = sum(nums)


        ranges = []
        p = 1
        
            
        while x * p <= total:
            ranges.append((x*p, (x+1) * p - 1))
            p *= 10

        buckets = [[] for _ in range(10)]
        buckets[0].append(0)

        cur = 0
        res = 0

        for num in nums:
            cur += num
            need = (cur % 10 - x) % 10

            arr = buckets[need]

            
            for L,R in ranges:
                 lo = cur - R
                 hi = cur - L

                 res += (bisect_right(arr, hi) - bisect_left(arr, lo)
                     )
            
            buckets[cur % 10].append(cur)

        return res