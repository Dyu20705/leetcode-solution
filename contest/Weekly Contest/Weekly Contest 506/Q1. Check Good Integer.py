class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0
        n_string = str(n)
        for i in range(len(n_string)):
            x = int(n_string[i])
            digitSum += x
            squareSum += (x * x)
        if squareSum - digitSum >= 50:
            return True
        else: return False