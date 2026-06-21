class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        if not 0 <= x <= 9:
            return 0

        n = len(nums)

        prefix = [0] * (n + 1)
        non_negative = True
        total = 0

        for i, value in enumerate(nums):
            if value < 0:
                non_negative = False

            total += value
            prefix[i + 1] = total

        if not non_negative:
            return self._quadratic(nums, x)

        if x == 0:
            frequency = {}
            ans = 0

            for value in prefix:
                ans += frequency.get(value, 0)
                frequency[value] = frequency.get(value, 0) + 1

            return ans

        ans = 0
        place = 1

        while x * place <= total:
            lower = x * place

            if place == 1:
                upper = x
            else:
                upper = (x + 1) * place - 1

            residue_count = [0] * 10

            add_ptr = 0
            remove_ptr = 0

            for right, current_prefix in enumerate(prefix):
                while (
                    add_ptr < right
                    and prefix[add_ptr] <= current_prefix - lower
                ):
                    residue_count[prefix[add_ptr] % 10] += 1
                    add_ptr += 1

                while (
                    remove_ptr < add_ptr
                    and prefix[remove_ptr] < current_prefix - upper
                ):
                    residue_count[prefix[remove_ptr] % 10] -= 1
                    remove_ptr += 1

                required_residue = (current_prefix - x) % 10
                ans += residue_count[required_residue]

            place *= 10

        return ans

    @staticmethod
    def _quadratic(nums: list[int], x: int) -> int:
        ans = 0
        n = len(nums)

        for left in range(n):
            current_sum = 0

            for right in range(left, n):
                current_sum += nums[right]

                if current_sum < 0:
                    continue

                if current_sum == 0:
                    ans += x == 0
                    continue

                if current_sum % 10 != x:
                    continue

                first_digit = current_sum
                while first_digit >= 10:
                    first_digit //= 10

                ans += first_digit == x

        return ans
    
'''
class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        if not 0 <= x <= 9:
            return 0

        ans = 0
        n = len(nums)

        for left in range(n):
            current_sum = 0

            for right in range(left, n):
                current_sum += nums[right]

                if current_sum < 0:
                    continue

                if current_sum == 0:
                    ans += x == 0
                    continue

                if current_sum % 10 != x:
                    continue

                first_digit = current_sum
                while first_digit >= 10:
                    first_digit //= 10

                if first_digit == x:
                    ans += 1

        return ans
'''