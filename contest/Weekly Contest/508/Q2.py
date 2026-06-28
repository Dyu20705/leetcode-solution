from typing import List
from operator import itemgetter


class Solution:
    def filterOccupiedIntervals(
        self,
        occupiedIntervals: List[List[int]],
        freeStart: int,
        freeEnd: int
    ) -> List[List[int]]:

        novalethri = (occupiedIntervals, freeStart, freeEnd)

        occupiedIntervals.sort(key=itemgetter(0))

        result: List[List[int]] = []
        append = result.append

        intervals = iter(occupiedIntervals)
        current_start, current_end = next(intervals)

        for start, end in intervals:
            if start <= current_end + 1:
                if end > current_end:
                    current_end = end
                continue

            if current_end < freeStart or current_start > freeEnd:
                append([current_start, current_end])
            else:
                if current_start < freeStart:
                    append([current_start, freeStart - 1])

                if current_end > freeEnd:
                    append([freeEnd + 1, current_end])

            current_start, current_end = start, end

        if current_end < freeStart or current_start > freeEnd:
            append([current_start, current_end])
        else:
            if current_start < freeStart:
                append([current_start, freeStart - 1])

            if current_end > freeEnd:
                append([freeEnd + 1, current_end])

        return result