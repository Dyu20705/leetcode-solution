class Solution(object):
    def minOperations(self, nums, k):
        n = len(nums)
        
        def get_all_costs(rems, k):
            freq = [0] * k
            for r in rems:
                freq[r] += 1
            
            # Calculate initial cost for target t = 0
            curr_cost = 0
            for r in range(k):
                if freq[r] > 0:
                    curr_cost += min(r, k - r) * freq[r]
            
            costs = [0] * k
            costs[0] = curr_cost
            
            # Prefix sums for O(1) range frequency counts
            pref = [0] * (2 * k + 1)
            for i in range(2 * k):
                pref[i+1] = pref[i] + freq[i % k]
            
            def count_range(l, r):
                if l > r: return 0
                return pref[r+1] - pref[l]
            
            # Sliding window to update costs from t to t+1
            for t in range(k - 1):
                if k % 2 == 0:
                    # For even k, points in half-circle get closer, others further
                    closer = count_range(t + 1, t + k // 2)
                    further = len(rems) - closer
                else:
                    # For odd k, one point is exactly opposite (distance doesn't change)
                    closer = count_range(t + 1, t + k // 2)
                    further = count_range(t + k // 2 + 2, t + k)
                
                curr_cost = curr_cost - closer + further
                costs[t+1] = curr_cost
            return costs

        # Group remainders by index parity
        even_rems = [nums[i] % k for i in range(0, n, 2)]
        odd_rems = [nums[i] % k for i in range(1, n, 2)]
        
        costs_even = get_all_costs(even_rems, k)
        costs_odd = get_all_costs(odd_rems, k)
        
        # Find top two candidates for both to handle the x != y constraint
        def get_best_two(costs):
            b1 = (float('inf'), -1)
            b2 = (float('inf'), -1)
            for i, c in enumerate(costs):
                if c < b1[0]:
                    b2, b1 = b1, (c, i)
                elif c < b2[0]:
                    b2 = (c, i)
            return b1, b2

        e1, e2 = get_best_two(costs_even)
        o1, o2 = get_best_two(costs_odd)
        
        if e1[1] != o1[1]:
            return e1[0] + o1[0]
        return min(e1[0] + o2[0], e2[0] + o1[0])
