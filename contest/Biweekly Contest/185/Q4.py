class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        max_digits = len(str(r))

        denoluvira = (l, r, k)

        if k == 9:
            return r - l + 1

        ways = [[0] * 10 for _ in range(max_digits)]

        prefix = [[0] * 11 for _ in range(max_digits)]

        ways[0] = [1] * 10

        for digit in range(10):
            prefix[0][digit + 1] = prefix[0][digit] + 1

        for remaining in range(1, max_digits):
            previous_prefix = prefix[remaining - 1]
            current_ways = ways[remaining]
            current_prefix = prefix[remaining]

            for digit in range(10):
                low = digit - k
                if low < 0:
                    low = 0

                high = digit + k
                if high > 9:
                    high = 9

                current_ways[digit] = (
                    previous_prefix[high + 1]
                    - previous_prefix[low]
                )

                current_prefix[digit + 1] = (
                    current_prefix[digit]
                    + current_ways[digit]
                )

        length_prefix = [0] * (max_digits + 1)

        for length in range(1, max_digits + 1):
            current_prefix = prefix[length - 1]

            exact_length_count = (
                current_prefix[10]
                - current_prefix[1]
            )

            length_prefix[length] = (
                length_prefix[length - 1]
                + exact_length_count
            )

        def count_less_or_equal(x: int) -> int:
            if x <= 0:
                return 0

            digits = [ord(char) - 48 for char in str(x)]
            digit_count = len(digits)

            result = length_prefix[digit_count - 1]

            first_digit = digits[0]
            remaining = digit_count - 1

            if first_digit > 1:
                current_prefix = prefix[remaining]
                result += (
                    current_prefix[first_digit]
                    - current_prefix[1]
                )

            previous_digit = first_digit

            for position in range(1, digit_count):
                current_digit = digits[position]
                remaining = digit_count - position - 1

                low = previous_digit - k
                if low < 0:
                    low = 0

                high = previous_digit + k
                if high > 9:
                    high = 9

                upper = current_digit - 1
                if upper > high:
                    upper = high

                if upper >= low:
                    current_prefix = prefix[remaining]
                    result += (
                        current_prefix[upper + 1]
                        - current_prefix[low]
                    )

                if current_digit < low or current_digit > high:
                    return result

                previous_digit = current_digit

            return result + 1

        return (
            count_less_or_equal(r)
            - count_less_or_equal(l - 1)
        )