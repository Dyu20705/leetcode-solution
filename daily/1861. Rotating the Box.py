class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        #Thiết kế 1:
        #Cho đá rơi sang phải luôn
        #Xoay ma trận 90 độ theo chiều kim đồng hồ
        # m, n = len(boxGrid), len(boxGrid[0])
        # for i in range(m):
        #     empty = n - 1
        #     for j in range(n - 1, -1, -1):
        #         if boxGrid[i][j] == '*':
        #             empty = j - 1
        #         elif boxGrid[i][j] == '#':
        #             boxGrid[i][j], boxGrid[i][empty] = '.', '#'
        #             empty -= 1
        
        # rotated = [['.'] * m for _ in range(n)]
        # for i in range(m):
        #     for j in range(n):
        #         rotated[j][m - 1 - i] = boxGrid[i][j]
        # return rotated
        #Thiết kế 2:
        m, n = len(boxGrid), len(boxGrid[0])
        rotated = [['.'] * m for _ in range(n)]

        for i in range(m):
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    rotated[j][m - 1 - i] = '*'
                    empty = j - 1
                elif boxGrid[i][j] == '#':
                    rotated[empty][m - 1 - i] = '#'
                    empty -= 1

        return rotated