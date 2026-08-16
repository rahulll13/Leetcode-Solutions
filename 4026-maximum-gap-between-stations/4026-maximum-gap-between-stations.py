class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n=len(skill)
        le=[0]*n
        ri=[0]*n
        j=0
        for i in range(n):
            while(station[j]!=skill[i]):
                j+=1
            le[i]=j
            j+=1
        j=len(station)-1
        for i in range(n-1,-1,-1):
            while(station[j]!=skill[i]):
                j-=1
            ri[i]=j
            j-=1
        ans=0
        for i in range(n-1):
            ans=max(ans,ri[i+1]-le[i])
        return ans