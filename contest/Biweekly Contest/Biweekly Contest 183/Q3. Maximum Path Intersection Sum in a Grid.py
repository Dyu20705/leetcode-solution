class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ans = -float('inf')
        for row in grid:
            cur = row[0]
            for val in row[1:]:
                if cur + val > ans:
                    ans = cur + val
                cur = val if cur < 0 else cur + val

        for col in zip(*grid):
            cur = col[0]
            for val in col[1:]:
                if cur + val > ans:
                    ans = cur + val
                cur = val if cur < 0 else cur + val

        for row in grid[1:-1]:
            for val in row[1:-1]:
                if val > ans:
                    ans = val
        return ans
            