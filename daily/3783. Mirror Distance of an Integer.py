class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return abs(n - int(str(n)[::-1]))
        # str(n) tạo object mới
        # [::1] tạo chuỗi mới
        # int() parse lại số
        # 3 lần allocate và xử lý O(k) với k là số chữ số của n
        # có thể làm trong O(1) bằng cách xử lý số nguyên trực tiếp
        x, rev = n, 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        return abs(n - rev)