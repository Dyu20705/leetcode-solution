class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        state = bytearray(n + 1)
        res = [0] * n
        common = 0

        for i in range(n):
            a = A[i]
            b = B[i]

            if not (state[a] & 1):
                state[a] |= 1
                if state[a] == 3:
                    common += 1
            if not (state[b] & 2):
                state[b] |= 2
                if state[b] == 3:
                    common += 1
            res[i] = common
        return res