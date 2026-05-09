class Solution:
    def minFlips(self, s: str) -> int:
        v = s # để dễ đọc hơn
        n = len(v) # độ dài chuỗi
        if n <=2: # nếu chuỗi có độ dài nhỏ hơn hoặc bằng 2, thì không thể chứa "011" và "110", nên không cần lật bit nào cả
            return 0
        t1 = v.count('1') # đếm số lượng bit 1 trong chuỗi
        t0 = n - t1 # số lượng bit 0 trong chuỗi

        res = t1 # nếu lật tất cả bit 1 thành bit 0, thì số lượng bit cần lật là số lượng bit 1

        res = min(res, t0) # nếu lật tất cả bit 0 thành bit 1, thì số lượng bit cần lật là số lượng bit 0

        if t1 > 0: # nếu có ít nhất một bit 1, thì ta có thể lật tất cả bit 1 thành bit 0, và sau đó lật một bit 0 thành bit 1 để tạo ra chuỗi chỉ chứa một loại bit, điều này sẽ không chứa "011" và "110", nên số lượng bit cần lật là số lượng bit 1 trừ đi 1
            res = min(res, t1 - 1)
        else: # nếu không có bit 1 nào, thì ta có thể lật tất cả bit 0 thành bit 1, và sau đó lật một bit 1 thành bit 0 để tạo ra chuỗi chỉ chứa một loại bit, điều này sẽ không chứa "011" và "110", nên số lượng bit cần lật là số lượng bit 0 trừ đi 1
            res = min(res, 1)

        cost_ends = (0 if v[0] == '1' else 1) + \
                (0 if v[n-1] == '1' else 1) + \
                v[1:n-1].count('1')
        #cost_end bằng tổng số bit 1 ở giữa chuỗi cộng với số bit 0 ở hai đầu chuỗi, vì nếu có một bit 0 ở đầu hoặc cuối chuỗi, thì ta có thể lật nó thành bit 1 để tạo ra chuỗi chỉ chứa một loại bit, điều này sẽ không chứa "011" và "110", nên số lượng bit cần lật là số lượng bit 1 ở giữa cộng với số bit 0 ở hai đầu chuỗi
        return min(res, cost_ends)