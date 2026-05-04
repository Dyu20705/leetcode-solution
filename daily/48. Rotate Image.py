class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Lật theo đường chéo chính
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #Lật theo đường thẳng đứng
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
        # Bước trên bằng:
        # for i in range(n):
        #     matrix[i].reverse()
        
        #Cách 2: Lật theo từng lớp
        # n = len(matrix)
        
        # for layer in range(n // 2):
        #     first = layer
        #     last = n - 1 - layer
            
        #     for i in range(first, last):
        #         offset = i - first
                
        #         top = matrix[first][i]
                
        #         matrix[first][i] = matrix[last - offset][first]
        #         matrix[last - offset][first] = matrix[last][last - offset]
        #         matrix[last][last - offset] = matrix[i][last]
        #         matrix[i][last] = top