class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0
        for c in s:
            if c == '*':
                if l > 0:
                    l -= 1
            elif c == '#':
                l *= 2
            elif c == '%':
                pass
            else:
                l += 1

        if k >= l:
            return '.'

        ptr = k
        for c in s[::-1]:
            if c == '*':
                l += 1
            elif c == '#':
                if ptr >= l // 2:
                    ptr -= l // 2
                l = l // 2
            elif c == '%':
                ptr = (l - 1) - ptr
            else:
                if l == ptr + 1:
                    return c
                l -= 1
        return s[ptr]