class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic={}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]]=[i]
            else:
                dic[arr[i]].append(i)
        st=[0]
        visited=[0]*len(arr)
        ans=0
        visited[0]=1
        while st:
            k=[]
            if visited[-1]==1:return ans
            ans+=1
            for i in st:
                if i!=0 and visited[i-1]==0:
                    
                    k.append(i-1)
                    visited[i-1]=1
                if i!=len(arr)-1 and visited[i+1]==0:
                    k.append(i+1)
                    visited[i+1]=1
                if arr[i] in dic:
                    for j in dic[arr[i]]:
                        if visited[j]==0:
                            k.append(j)
                            visited[j]=1
                    del dic[arr[i]]
            st=k




        