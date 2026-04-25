from bisect import bisect_left


class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = []
        
        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(side * 3 - y)
            else:
                arr.append(side * 4 - x)
        
        arr.sort()
        
        def check(limit):
            perimeter = side * 4
            for start in arr:
                end = start + perimeter - limit
                cur = start
                for _ in range(k - 1):
                    idx = bisect_left(arr, cur + limit)
                    if idx == len(arr) or arr[idx] > end:
                        cur = -1
                        break
                    cur = arr[idx]
                if cur >= 0:
                    return True
            return False
        
        lo, hi = 1, side
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
                ans = mid
            else:
                hi = mid - 1
                
        return ans