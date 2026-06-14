class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        n_nonneg = sum(num >= 0 for num in nums)
        
        if n_nonneg == 0:
            return max(nums)

        if n_nonneg >= n - k:
            return sum(num for num in nums if num >= 0)

        sorted_vals = sorted([(num, -ind) for ind, num in enumerate(nums)], reverse = True)
        ranks = [None] * n
        for rnk, (_, ind) in enumerate(sorted_vals):
            ranks[-ind] = rnk

        ans = -10 ** 9
        for l in range(n):
            raw_sum = 0
            worst_vals_sum = 0
            best_vals_sum = 0
            best_vals_admitted = 0
            
            pq = []
            ranks_used = [False] * n
            for r in range(l, n):
                raw_sum += nums[r]
                
                heappush(pq, (-nums[r], ranks[r]))
                worst_vals_sum += nums[r]
                if len(pq) > k:
                    popped_val, popped_rank = heappop(pq)
                    popped_val = -popped_val
                    worst_vals_sum -= popped_val
                    ranks_used[popped_rank] = True

                    if popped_rank < best_vals_admitted:
                        best_vals_sum -= sorted_vals[popped_rank][0]
                        while ranks_used[best_vals_admitted]:
                            best_vals_admitted += 1
                        best_vals_sum += sorted_vals[best_vals_admitted][0]
                        best_vals_admitted += 1
                
                else:
                    best_vals_admitted += 1
                    best_vals_sum += sorted_vals[best_vals_admitted - 1][0]
                #print(l, r, pq, raw_sum, worst_vals_sum, best_vals_sum, raw_sum - worst_vals_sum + best_vals_sum)
                
                ans = max(ans, raw_sum - worst_vals_sum + best_vals_sum)
                
        
        return ans