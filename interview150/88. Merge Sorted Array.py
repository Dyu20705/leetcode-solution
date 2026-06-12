'''
Giải thích cách giải:
i,j,k: 3 con trỏ
i: trỏ đến phần tử cuối cùng của nums1 (m-1)
j: trỏ đến phần tử cuối cùng của nums2 (n-1)
k: trỏ đến phần tử cuối cùng của nums1 (m+n-1)
Bắt đầu từ cuối cùng của nums1 và nums2, so sánh phần tử tại i và j
Nếu nums1[i] > nums2[j], gán nums1[k] = nums1[i], giảm i và k
Ngược lại, gán nums1[k] = nums2[j], giảm j và k
Tiếp tục quá trình này cho đến khi một trong hai con trỏ i hoặc j hết phần tử
Nếu j vẫn còn phần tử, gán nums1[k] = nums2[j], giảm j và k
Cuối cùng, nums1 sẽ chứa tất cả phần tử đã được sắp xếp
Độ phức tạp thời gian: O(m + n) vì chúng ta duyệt qua cả hai mảng một lần
Độ phức tạp không gian: O(1) vì chúng ta chỉ sử dụng một số biến phụ để lưu trữ con trỏ
Ví dụ:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Giải thích:
So sánh 3 và 6, gán nums1[5] = 6, giảm j và k: j = 2, k = 4
So sánh 3 và 5, gán nums1[4] = 5, giảm j và k: j = 1, k = 3
So sánh 3 và 2, gán nums1[3] = 3, giảm i và k: i = 2, k = 2
So sánh 2 và 2, gán nums1[2] = 2, giảm j và k: j = 0, k = 1
So sánh 2 và 1, gán nums1[1] = 2, giảm j và k: j = -1, k = 0
j đã hết phần tử, dừng lại
Kết quả cuối cùng: nums1 = [1,2,2,3,5,6]
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        