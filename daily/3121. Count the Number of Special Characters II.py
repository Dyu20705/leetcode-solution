class Solution(object): 
    def numberOfSpecialChars(self, word): 
        """ :type word: str :rtype: int """ 
        lower = {} 
        upper = {} 
        for i, c in enumerate(word): 
            if c.islower(): 
                lower[c] = i 
            else: 
                if c not in upper: 
                    upper[c] = i 
        ans = 0 
        for c in string.ascii_lowercase: 
            if c in lower and c.upper() in upper and lower[c] < upper[c.upper()]: 
                ans += 1 
        return ans