class Solution(object): 
    def canReach(self, arr, start): 
        """ 
        :type arr: List[int] 
        :type start: int :rtype: bool 
        """ 
        if 0 not in arr: 
            return False 
        if start == 0: 
            return True 
        n = len(arr) 
        def valid(jump): 
            return 0 <= jump < n 
        queue = deque([start]) 
        seen = set([start]) 
        while queue: 
            curr = queue.popleft() 
            if arr[curr] == 0: 
                return True 
            jumpP = curr + arr[curr] 
            jumpM = curr - arr[curr] 
            if valid(jumpP) and jumpP not in seen: 
                queue.append(jumpP) 
                seen.add(jumpP) 
            if valid(jumpM) and jumpM not in seen: 
                queue.append(jumpM) 
                seen.add(jumpM) 
        return False