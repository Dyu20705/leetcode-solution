from bisect import bisect_right

MAX_DIGITS = 16
ASCII_SIZE = 58

def build_tables():
    tables = []

    for k in range(10):
        dp = [[0] * 10 for _ in range(MAX_DIGITS + 1)]
        dp[1] = [1] * 10

        for length in range(2, MAX_DIGITS + 1):
            previous = dp[length - 1]
            current = dp[length]

            prefix = [0] * 11
            running = 0

            for digit in range(10):
                running += previous[digit]
                prefix[digit + 1] = running

            for digit in range(10):
                left = digit - k
                if left < 0:
                    left = 0

                right = digit + k + 1
                if right > 10:
                    right = 10

                current[digit] = prefix[right] - prefix[left]

        base = [[0] * ASCII_SIZE for _ in range(MAX_DIGITS + 1)]

        shorter_count = 0

        for length in range(1, MAX_DIGITS + 1):
            count = shorter_count

            for first_digit in range(1, 10):
                base[length][48 + first_digit] = count
                count += dp[length][first_digit]

            shorter_count = count

        dp_prefix = [[0] * 11 for _ in range(MAX_DIGITS + 1)]

        for remaining in range(1, MAX_DIGITS + 1):
            running = 0
            row = dp[remaining]
            prefix = dp_prefix[remaining]

            for digit in range(10):
                running += row[digit]
                prefix[digit + 1] = running

        step = [
            [[None] * ASCII_SIZE for _ in range(ASCII_SIZE)]
            for _ in range(MAX_DIGITS + 1)
        ]

        for remaining in range(1, MAX_DIGITS + 1):
            prefix = dp_prefix[remaining]
            layer = step[remaining]

            for previous in range(10):
                valid_left = previous - k
                if valid_left < 0:
                    valid_left = 0

                valid_right = previous + k
                if valid_right > 9:
                    valid_right = 9

                transition_row = layer[48 + previous]

                for current in range(10):
                    smaller_right = current - 1

                    if smaller_right > valid_right:
                        smaller_right = valid_right

                    if smaller_right >= valid_left:
                        contribution = (
                            prefix[smaller_right + 1]
                            - prefix[valid_left]
                        )
                    else:
                        contribution = 0

                    valid = valid_left <= current <= valid_right

                    transition_row[48 + current] = (
                        contribution,
                        valid,
                    )

        tables.append((base, step))

    return tuple(tables)


TABLES = build_tables()

REP_DIGIT_NUMBERS = []

for digit in range(1, 10):
    value = 0

    for _ in range(MAX_DIGITS):
        value = value * 10 + digit
        REP_DIGIT_NUMBERS.append(value)

REP_DIGIT_NUMBERS.sort()
REP_DIGIT_NUMBERS = tuple(REP_DIGIT_NUMBERS)


def count_upto(x: int, base, step) -> int:

    if x <= 0:
        return 0

    if x < 10:
        return x

    text = str(x)
    length = len(text)

    previous = ord(text[0])

    total = base[length][previous]

    for index in range(1, length):
        current = ord(text[index])

        contribution, valid = step[length - index][previous][current]
        total += contribution

        if not valid:
            return total

        previous = current

    return total + 1


class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        if k == 9:
            return max(r, 0) - max(l - 1, 0)

        if k == 0:
            return (
                bisect_right(REP_DIGIT_NUMBERS, r)
                - bisect_right(REP_DIGIT_NUMBERS, l - 1)
            )

        base, step = TABLES[k]

        return (
            count_upto(r, base, step)
            - count_upto(l - 1, base, step)
        )