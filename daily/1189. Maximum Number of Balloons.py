class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = a = l = o = n = 0

        for char in text:
            if char == 'b':
                b += 1
            elif char == 'a':
                a += 1
            elif char == 'l':
                l += 1
            elif char == 'o':
                o += 1
            elif char == 'n':
                n += 1

        return min(b, a, l // 2, o // 2, n)