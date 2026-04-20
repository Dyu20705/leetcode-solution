class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        res, l, a, b = 0, len(colors), colors[0], colors[l-1]
        for i in range(l - 1, -1, -1):
            if(a!= colors[i]):
                res = max(res,i)
                break
        for i in range(0, l-1):
            if(b != colors[i]):
                res = max(res,l-1-i)
                break
        return res