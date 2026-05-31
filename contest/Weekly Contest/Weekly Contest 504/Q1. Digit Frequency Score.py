from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        #Chuyển số thành chuỗi và đếm tần suất của mỗi chữ số
        b = str(n).encode()
        #encode() hoạt động: Chuyển chuỗi thành một đối tượng bytes, trong đó mỗi ký tự được mã hóa thành một giá trị byte tương ứng. Ví dụ, '0' sẽ được mã hóa thành 48, '1' thành 49, và cứ tiếp tục như vậy cho đến '9' là 57.
        return sum(b) - 48 * len(b) #Tổng giá trị byte của các chữ số trừ đi 48 nhân với số lượng chữ số, vì mỗi chữ số được mã hóa thành một giá trị byte bắt đầu từ 48.