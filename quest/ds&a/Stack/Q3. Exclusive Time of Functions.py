from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev = 0

        res_loc = res
        stack_append = stack.append
        stack_pop = stack.pop

        for log in logs:
            c = log.find(':')
            func_id = int(log[:c])

            if log[c + 1] == 's':
                t = int(log[c + 7:])
                if stack:
                    res_loc[stack[-1]] += t - prev
                stack_append(func_id)
                prev = t
            else:
                t = int(log[c + 5:])
                res_loc[stack_pop()] += t - prev + 1
                prev = t + 1

        return res