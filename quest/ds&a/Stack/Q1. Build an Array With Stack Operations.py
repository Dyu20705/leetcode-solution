class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        append = res.append
        p=0
        end = target[-1]
        for i in range(1, end + 1):
            append("Push")
            if i == target[p]:
                p += 1
            else:
                append("Pop")
        return res