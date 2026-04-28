class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        #1
        # flat = [num for row in grid for num in row]
        # flat.sort()
        # med = flat[len(flat) // 2]
        # if any((num - med) % x for num in flat):
        #     return -1
        # return sum(abs(num - med) for num in flat) // x

        #2
        # flat = []
        # mod = grid[0][0] % x
        # for row in grid:
        #     for num in row:
        #         if num % x != mod:
        #             return -1
        #         flat.append(num)
        # flat.sort()
        # med = flat[len(flat) // 2]
        # return sum(abs(num - med) for num in flat) // x

        #3
        flat = []
        mod = grid[0][0] % x
        for row in grid:
            for num in row:
                if num % x != mod:
                    return -1
                flat.append(num)
        flat.sort()
        med = flat[len(flat) // 2]
        ops = 0
        for num in flat:
            ops += abs(num - med) // x
        return ops
