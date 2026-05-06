class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lenN = len(nums)
        #Duyệt mảng và đánh dấu các số đã xuất hiện bằng cách đổi dấu của phần tử tại vị trí tương ứng
        for i in range(lenN):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        #Duyệt lại mảng để tìm các số chưa xuất hiện (các phần tử vẫn dương)
        result = []
        for i in range(lenN):
            if nums[i] > 0:
                result.append(i + 1)

        return result
        # Ví dụ sử dụng
        #nums = [4,3,2,7,8,2,3,1]
        #chạy qua vòng lặp
        #i = 0, index = 3, nums = [4,3,2,-7,8,2,3,1]
        #i = 1, index = 2, nums = [4,3,-2,-7,8,2,3,1]
        #i = 2, index = 1, nums = [4,-3,-2,-7,8,2,3,1]
        #i = 3, index = 6, nums = [4,-3,-2,-7,8,2,-3,1]
        #i = 4, index = 7, nums = [4,-3,-2,-7,8,2,-3,-1]
        #i = 5, index = 1, nums = [4,-3,-2,-7,8,2,-3,-1]
        #i = 6, index = 2, nums = [4,-3,-2,-7,8,2,-3,-1]
        #i = 7, index = 0, nums = [-4,-3,-2,-7,8,2,-3,-1]
        #Duyệt lại mảng để tìm các số chưa xuất hiện
        #i = 0, nums[0] = -4 (đã xuất hiện)
        #i = 1, nums[1] = -3 (đã xuất hiện)
        #i = 2, nums[2] = -2 (đã xuất hiện)
        #i = 3, nums[3] = -7 (đã xuất hiện)
        #i = 4, nums[4] = 8 (chưa xuất hiện, thêm 5 vào kết quả)
        #i = 5, nums[5] = 2 (đã xuất hiện)
        #i = 6, nums[6] = -3 (đã xuất hiện)
        #i = 7, nums[7] = -1 (đã xuất hiện)
        #Kết quả cuối cùng: [5, 6]
        #Tại sao lại hoạt động?
        #Bởi vì chúng ta sử dụng giá trị của phần tử để đánh dấu sự xuất hiện của số tương ứng.
        #Khi chúng ta gặp một số, chúng ta đổi dấu của phần tử tại vị trí tương ứng để đánh dấu rằng số đó đã xuất hiện.
        #Cuối cùng, chúng ta chỉ cần kiểm tra các phần tử còn dương để tìm ra những số chưa xuất hiện.
        #Cách 2: xử lý bit
        # lenN = len(nums)
        # a = 0
        # for num in nums:
        #     a |= 1 << (num - 1)
        # result = []
        # for i in range(lenN):
        #     if (a & (1 << i)) == 0:
        #         result.append(i + 1)
        # return result
    