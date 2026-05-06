class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        sorted_nums = sorted(nums)
        #Có cách giải kiểu như:
        #Xét phần tử thứ nhất của mảng đã sắp xếp (nó là lớn nhất)
        #Nên nó nhận giá trị len(nums) - 1,
        #Sau đó xet phần tử thứ 2 của mảng đã sắp xếp (nếu nó khác phần tử thứ nhất thì nó nhận giá trị len(nums) - 2
        #Nếu nó bằng phần tử thứ nhất thì nó nhận giá trị len(nums) - 1)
        #Cứ như vậy đến phần tử cuối cùng của mảng đã sắp xếp.
        #Sau đó ta sẽ có một dictionary lưu lại số lượng phần tử nhỏ hơn mỗi phần tử trong mảng đã sắp xếp.
        #Cuối cùng ta sẽ duyệt qua mảng nums và lấy giá trị từ dictionary để trả về kết quả.
        count_dict = {}

        for i in range(len_nums):
            if sorted_nums[i] not in count_dict:
                count_dict[sorted_nums[i]] = i
        result = []
        for num in nums:
            result.append(count_dict[num])
        return result