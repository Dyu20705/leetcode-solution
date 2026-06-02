from operator import add
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        inf = float('inf')

        if n <= m:
            minLandEnd = min(map(add, landStartTime, landDuration))
            minWaterEnd = inf
            min_land_time = inf
            for ws, wd in zip(waterStartTime, waterDuration):
                end = ws + wd
                if end < minWaterEnd:
                    minWaterEnd = end
                t = (ws if ws >= minLandEnd else minLandEnd) + wd
                if t < min_land_time:
                    min_land_time = t

            min_water_time = inf
            for ls, ld in zip(landStartTime, landDuration):
                t = (ls if ls >= minWaterEnd else minWaterEnd) + ld
                if t < min_water_time:
                    min_water_time = t
        else:
            minWaterEnd = min(map(add, waterStartTime, waterDuration))

            minLandEnd = inf
            min_water_time = inf
            for ls, ld in zip(landStartTime, landDuration):
                end = ls + ld
                if end < minLandEnd:
                    minLandEnd = end
                t = (ls if ls >= minWaterEnd else minWaterEnd) + ld
                if t < min_water_time:
                    min_water_time = t

            min_land_time = inf
            for ws, wd in zip(waterStartTime, waterDuration):
                t = (ws if ws >= minLandEnd else minLandEnd) + wd
                if t < min_land_time:
                    min_land_time = t

        return min_land_time if min_land_time < min_water_time else min_water_time