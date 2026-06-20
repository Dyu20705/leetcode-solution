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