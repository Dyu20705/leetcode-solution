class Solution(object):
    def passwordStrength(self, password):
        """
        :type password: str
        :rtype: int
        """
        p = set(password)
        t = 0
        for c in p:
            if c.islower():
                t += 1
            elif c.isupper():
                t += 2
            elif c.isdigit():
                t += 3
            else:
                t += 5
        return t