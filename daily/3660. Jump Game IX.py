class Solution(object):
    def maxValue(self, nums):
        '''
        Bạn được cung cấp một mảng số nguyên nums.
        Từ bất kỳ chỉ mục nào i, bạn có thể chuyển đến một chỉ mục khác jtheo các quy tắc sau:
        Chuyển đến mục lục jnơi j > ichỉ được phép nếu nums[j] < nums[i].
        Chuyển đến mục lục jnơi j < ichỉ được phép nếu nums[j] > nums[i].
        Với mỗi chỉ số i, hãy tìm giá trị lớn nhất có thể đạt được bằng cách thực hiện bất kỳ chuỗi bước nhảy hợp lệ nào bắt đầu từ .numsi
        Trả về một mảng anstrong đó ans[i]là giá trị lớn nhất có thể đạt được bắt đầu từ chỉ số .i
        '''
        #Ý tưởng giải bài toán của tôi:
        #Đầu tiên, tôi sẽ tạo một mảng res có cùng kích thước với nums để lưu trữ kết quả.
        #Tôi sẽ đi qua mảng nums từ phải sang trái để tính giá trị lớn nhất có thể đạt được từ mỗi chỉ số i.
        #Tôi sẽ sử dụng một biến cur_max để theo dõi giá trị lớn nhất hiện tại mà tôi có thể đạt được từ chỉ số i.
        #Nếu nums[i] lớn hơn cur_max, tôi sẽ cập nhật cur_max và tiếp tục đi qua mảng.
        #Nếu cur_max nhỏ hơn hoặc bằng res[i + 1], tôi sẽ cập nhật res[j] cho tất cả j từ start đến i bằng cur_max và cập nhật start thành i + 1.
        #Cuối cùng, tôi sẽ kiểm tra nếu nums[-1] lớn hơn cur_max và cập nhật res[j] cho tất cả j từ start đến n bằng cur_max nếu cần thiết.
        #Kết quả cuối cùng sẽ được trả về trong mảng res.
        n = len(nums)
        if n == 0:
            return []

        res = [0] * n
        res[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            nxt = res[i + 1]
            res[i] = nums[i] if nums[i] < nxt else nxt

        start = 0
        cur_max = nums[0]

        for i in range(n - 1):
            if nums[i] > cur_max:
                cur_max = nums[i]

            if cur_max <= res[i + 1]:

                for j in range(start, i + 1):
                    res[j] = cur_max

                start = i + 1

                if start < n:
                    cur_max = nums[start]

        if nums[-1] > cur_max:
            cur_max = nums[-1]

        for j in range(start, n):
            res[j] = cur_max

        return res