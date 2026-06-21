MOD = 1_000_000_007

class Solution:
    def maxTotalValue(
        self,
        value: list[int],
        decay: list[int],
        m: int
    ) -> int:
        max_value = max(value)

        # zireluntha = (value, decay, m)

        positive_count = 0
        positive_sum = 0

        for initial, step in zip(value, decay):
            count = (initial - 1) // step + 1

            positive_count += count
            positive_sum += (
                count * initial
                - step * count * (count - 1) // 2
            )

            if positive_count >= m:
                break

        if positive_count < m:
            return positive_sum % MOD

        low = 1
        high = max_value

        while low < high:
            mid = (low + high + 1) >> 1

            count = 0

            for initial, step in zip(value, decay):
                if initial >= mid:
                    count += (initial - mid) // step + 1

                    if count >= m:
                        break

            if count >= m:
                low = mid
            else:
                high = mid - 1

        threshold = low

        count = 0
        total = 0

        for initial, step in zip(value, decay):
            if initial >= threshold:
                taken = (initial - threshold) // step + 1

                count += taken
                total += (
                    taken * initial
                    - step * taken * (taken - 1) // 2
                )

        total -= (count - m) * threshold

        return total % MOD