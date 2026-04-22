class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        res = []
        for query in queries:
            for word in dictionary:
                diff = sum(1 for a, b in zip(query, word) if a != b)
                if diff <= 2:
                    res.append(query)
                    break
        return res