class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        if n == 0:
            return 0
        diff = [0] * (n + 1)
        for i, radius in enumerate(lights):
            if radius ==0:
                continue
            left = max(0, i - radius)
            right = min(n, i + radius+1)
            diff[left] += 1
            diff[right] -= 1
        cnt = 0
        ec = 0
        ace = -1
        for i in range(n):
            ec += diff[i]
            if ec > 0:
                continue
            if i <= ace:
                continue
            cnt += 1
            ace = i + 2
        return cnt
'''
top1:
class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        max_lit = 0
        segments = []
        for i in range(n):
            v = lights[i]
            if 0 == v:
                continue
            start = max(0, i - v) - 1
            if start >= max_lit:
                segments.append((max_lit, start))
            else:
                seg_len = len(segments)
                if seg_len > 0:
                    for j in range(seg_len - 1, -1, -1):
                        old_start, old_end = segments[j]
                        if start < old_start:
                            segments.pop(-1)
                            continue
                        new_end = min(old_end, start)
                        segments[j] = (old_start, new_end)
                        break
            new_max_lit = min(n - 1, i + v) + 1
            if new_max_lit > max_lit:
                max_lit = new_max_lit
        if max_lit <= n - 1:
            segments.append((max_lit, n - 1))
        output = 0
        for unlit_start, unlit_end in segments:
            count_unlit = unlit_end - unlit_start + 1
            output += math.ceil(count_unlit / 3.0)
        return output
'''