class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #tại sao lại phải đổi ngược trước?
        #vì khi đếm số lượng chẵn lẻ ở phía sau, nếu đi từ trái sang phải thì sẽ không biết được số lượng chẵn lẻ ở phía sau, còn nếu đi từ phải sang trái thì sẽ biết được số lượng chẵn lẻ ở phía sau ngay khi gặp một số, từ đó có thể cập nhật kết quả cho số đó một cách chính xác.
        # nums = nums[::-1]
        # even_count = 0
        # odd_count = 0
        # result = []
        # for num in nums:
        #     if num % 2 ==0:
        #         even_count +=1
        #     else:
        #         odd_count +=1
        #     result.append(odd_count if num % 2 ==0 else even_count)
        # return result[::-1]
        even_count = 0
        odd_count = 0
        lenN = len(nums)
        result = [0] * lenN
        for i in range(lenN-1, -1, -1):
            if nums[i] % 2 ==0:
                even_count +=1
            else:
                odd_count +=1
            result[i] = odd_count if nums[i] % 2 ==0 else even_count
        return result
