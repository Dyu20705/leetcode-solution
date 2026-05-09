class Solution(object):
    # def isPrime(self, n):
    #     if n <= 1:
    #         return False
    #     for i in range(2, int(n**0.5) + 1):
    #         if n % i == 0:
    #             return False
    #     return True
    # def sumOfPrimesInRange(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     r = int(str(n)[::-1])
    #     start, end = min(n, r), max(n, r)
    #     total = 0
    #     for i in range(start, end + 1):
    #         if self.isPrime(i):
    #             total += i
    #     return total
    def sumOfPrimesInRange(self, n):
        r = int(str(n)[::-1])
        start, end = min(n, r), max(n, r)
        if end < 2:
            return 0
        sieve = [True] * (end + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(end**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, end + 1, i):
                    sieve[j] = False
        total = sum(i for i in range(start, end + 1) if sieve[i])
        return total
    
