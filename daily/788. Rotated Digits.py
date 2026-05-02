'''2 phương pháp:
1. Brute Force: Duyệt qua tất cả các số từ 1 đến n, kiểm tra xem mỗi số có phải là một số "rotated" hợp lệ hay không.
2. Dynamic Programming (DP): Sử dụng một hàm đệ quy với memoization để đếm số lượng số "rotated" hợp lệ từ 1 đến n. 
Hàm này sẽ kiểm tra từng chữ số của n và quyết định xem có thể chọn chữ số đó hay không, đồng thời theo dõi xem đã sử dụng ít nhất một chữ số khác nhau chưa.'''
class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # cnt = 0
        # for i in range(1, n + 1):
        #     s = str(i)
        #     if '3' in s or '4' in s or '7' in s:
        #         continue
        #     if '2' in s or '5' in s or '6' in s or '9' in s:
        #         cnt += 1
        # return cnt
        s = str(n)

        same = {'0', '1', '8'}
        diff = {'2', '5', '6', '9'}
        valid = same | diff
        def dp(pos, tight, changed, started):
            #pos: là vị trí hiện tại đang xét trong chuỗi số n (bắt đầu từ 0)
            #tight: là một biến boolean cho biết liệu chúng ta có đang bị giới hạn bởi số n hay không (nếu tight là True, chúng ta chỉ có thể chọn các chữ số nhỏ hơn hoặc bằng chữ số tại vị trí pos trong n)
            #changed: là một biến boolean cho biết liệu chúng ta đã sử dụng ít nhất một chữ số khác nhau (2, 5, 6, 9) hay chưa (để đảm bảo rằng số đó là một số "rotated" hợp lệ)
            #started: là một biến boolean cho biết liệu chúng ta đã bắt đầu xây dựng số hay chưa (để tránh đếm các số bắt đầu bằng 0)
            if pos == len(s):
                return 1 if changed else 0
            limit = int(s[pos]) if tight else 9
            ressult = 0
            for digit in range(limit + 1):
                ch = str(digit)
                new_tight = tight and (digit == limit)

                if not started and ch == '0':
                    ressult += dp(pos + 1, new_tight, changed, False)
                else:
                    if ch in valid:
                        ressult += dp(pos + 1, new_tight, changed or (ch in diff), True)
            return ressult
        
        return dp(0, True, False, False)