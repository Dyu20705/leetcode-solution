class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n=len(cost)
        took=0
        ans=0
        for i in range(n-1,-1,-1):
            if took==2:
                took=0
            else:
                ans+=cost[i]
                took+=1
        return ans

        