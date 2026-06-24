class Solution:
    MOD = 1_000_000_007

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        m = r - l + 1

        if n == 1:
            return m
        d = m - 1
        sequence = [0] * (2 * d)
        vector = [1] * d

        for t in range(2 * d):
            sequence[t] = sum(vector) % MOD

            nxt = [0] * d
            prefix = 0
            target = d - 1

            for value in vector:
                prefix += value
                if prefix >= MOD:
                    prefix -= MOD

                nxt[target] = prefix
                target -= 1

            vector = nxt
        C = [1]
        B = [1]

        length = 0
        shift = 1
        last_discrepancy = 1

        for index in range(len(sequence)):
            discrepancy = sequence[index]

            for i in range(1, length + 1):
                discrepancy += C[i] * sequence[index - i]

            discrepancy %= MOD

            if discrepancy == 0:
                shift += 1
                continue

            old_C = C[:]

            coefficient = (
                discrepancy
                * pow(last_discrepancy, MOD - 2, MOD)
                % MOD
            )

            required_length = len(B) + shift
            if len(C) < required_length:
                C.extend([0] * (required_length - len(C)))

            for i, value in enumerate(B):
                C[i + shift] = (
                    C[i + shift] - coefficient * value
                ) % MOD

            if 2 * length <= index:
                length = index + 1 - length
                B = old_C
                last_discrepancy = discrepancy
                shift = 1
            else:
                shift += 1

        recurrence = [
            (-C[i]) % MOD
            for i in range(1, length + 1)
        ]

        initial = sequence[:length]

        k = length
        rec = recurrence

        def combine(a, b):
            product = [0] * (2 * k - 1)
            for i in range(k):
                ai = a[i]

                if ai:
                    for j in range(k):
                        product[i + j] += ai * b[j]

            for degree in range(2 * k - 2, k - 1, -1):
                value = product[degree] % MOD

                if value:
                    destination = degree - 1

                    for j in range(k):
                        product[destination - j] += value * rec[j]

            for i in range(k):
                product[i] %= MOD

            return product[:k]

        exponent = n - 1

        result_poly = [0] * k
        result_poly[0] = 1

        if k == 1:
            base_poly = [rec[0]]
        else:
            base_poly = [0] * k
            base_poly[1] = 1

        while exponent:
            if exponent & 1:
                result_poly = combine(result_poly, base_poly)

            exponent >>= 1

            if exponent:
                base_poly = combine(base_poly, base_poly)

        answer = 0

        for coefficient, value in zip(result_poly, initial):
            answer += coefficient * value

        return (2 * (answer % MOD)) % MOD