from typing import List

#Phương pháp giải
#1. Xác định các lớp của lưới: Lưới có thể được chia thành các lớp (layers) dựa trên khoảng cách từ biên ngoài. Mỗi lớp sẽ được xoay độc lập.
#2. Trích xuất phần tử của mỗi lớp: Đối với mỗi lớp, trích xuất các phần tử theo thứ tự: trên cùng (từ trái sang phải), bên phải (từ trên xuống dưới), dưới cùng (từ phải sang trái), và bên trái (từ dưới lên trên).
#3. Xoay phần tử: Sử dụng phép xoay vòng để di chuyển phần tử trong lớp. Số lần xoay được tính bằng k mod độ dài của lớp.
#4. Gán lại phần tử đã xoay vào vị trí mới: Sau khi xoay, gán lại các phần tử vào vị trí mới trong lớp.
#Độ phức tạp thời gian: O(m*n) vì chúng ta cần duyệt qua tất cả phần tử của lưới một lần để trích xuất và gán lại.
#Độ phức tạp không gian: O(m*n) trong trường hợp xấu nhất khi tất cả phần tử của lưới nằm trong một lớp duy nhất, nhưng thường sẽ là O(min(m, n)) do số phần tử trong mỗi lớp giảm dần khi chúng ta đi vào các lớp sâu hơn.
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        g = grid
        m = len(g)
        n = len(g[0])

        for layer in range(min(m, n) // 2):
            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            vals = []

            # top
            vals.extend(g[top][left:right + 1])

            # right
            for r in range(top + 1, bottom):
                vals.append(g[r][right])

            # bottom
            vals.extend(g[bottom][left:right + 1][::-1])

            # left
            for r in range(bottom - 1, top, -1):
                vals.append(g[r][left])

            L = len(vals)
            kk = k % L

            if kk:
                vals = vals[kk:] + vals[:kk]

            idx = 0

            # top
            row = g[top]
            for c in range(left, right + 1):
                row[c] = vals[idx]
                idx += 1

            # right
            for r in range(top + 1, bottom):
                g[r][right] = vals[idx]
                idx += 1

            # bottom
            row = g[bottom]
            for c in range(right, left - 1, -1):
                row[c] = vals[idx]
                idx += 1

            # left
            for r in range(bottom - 1, top, -1):
                g[r][left] = vals[idx]
                idx += 1

        return g