class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        if n<=1:
            return 1 if k==0 else 0
        t=sum(s[i]==s[(i+1)%n] for i in range(n))
        if k==t-1:
            return t
        elif k==t:
            return n-t
        else:
            return 0