class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        if s[-1] == "1":
            return False

        n = len(s)
        dq = deque([0])         # can be reached
        left_bound = n - 1 - maxJump
        right_bound = n - 1 - minJump

        i = 1
        while i < n:
            if s[i] == "1":
                i += 1
                continue

            while dq and dq[0] + maxJump < i:
                dq.popleft()
            if not dq:
                return False

            if dq[0] + minJump <= i:
                if i == n-1 or (left_bound <= i <= right_bound):
                    return True
                dq.append(i)
            i += 1

        return False
