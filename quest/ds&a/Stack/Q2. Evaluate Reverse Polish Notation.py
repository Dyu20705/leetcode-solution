from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = [0] * n
        top = -1
        ops = {'+', '-', '*', '/'}
        
        s_append = stack.__setitem__
        
        for token in tokens:
            if token in ops:
                b = stack[top]
                a = stack[top - 1]
                top -= 1
                if token == '+':
                    stack[top] = a + b
                elif token == '-':
                    stack[top] = a - b
                elif token == '*':
                    stack[top] = a * b
                else:
                    if a < 0 and b < 0 or a > 0 and b > 0:
                        stack[top] = abs(a) // abs(b)
                    else:
                        stack[top] = -(abs(a) // abs(b))
            else:
                top += 1
                stack[top] = int(token)

        return stack[top]