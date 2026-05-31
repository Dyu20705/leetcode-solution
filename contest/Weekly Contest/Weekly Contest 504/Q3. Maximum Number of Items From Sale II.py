class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(item[0] for item in items)
        freq = [0]*(max_f + 1)

        min_price = float('inf')
        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p

        multiples = [0]*(max_f + 1)
        for f in range(1, max_f +1):
            if freq[f] > 0:
                count = 0
                for k in range(f, max_f + 1, f):
                    count += freq[k]
                multiples[f] = count

        deal_counts = {}
        for f, p in items:
            c = multiples[f]-1
            if c>0 and p<2*min_price:
                deal_counts[p] = deal_counts.get(p, 0) + c

        ans = budget // min_price
        sorted_prices = sorted(deal_counts.keys())

        curr_w =0
        curr_k =0

        for p in sorted_prices:
            c = deal_counts[p]
            if curr_w + c * p <= budget:
                curr_w += c * p
                curr_k += c
                ans = max(ans, curr_k * 2 + (budget - curr_w) // min_price)
            else:
                affordable = (budget - curr_w) // p
                curr_w += affordable * p
                curr_k += affordable
                ans = max(ans, curr_k * 2 + (budget - curr_w) // min_price)
                break

        return ans