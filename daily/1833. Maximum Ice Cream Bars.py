class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        count = [0] * 100_001

        lo = 100_001
        hi = 0

        for cost in costs:
            count[cost] += 1
            if cost < lo:
                lo = cost
            if cost > hi:
                hi = cost

        bars = 0
        hi = min(hi, coins)

        for cost in range(lo, hi + 1):
            quantity = count[cost]

            if quantity:
                affordable = coins // cost

                if affordable < quantity:
                    return bars + affordable

                bars += quantity
                coins -= quantity * cost

        return bars