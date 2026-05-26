class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        s = set(word)
        cnt = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in s and c.upper() in s:
                cnt += 1
        return cnt