class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        n = len(s)
        for i in range(n):
            frequency = {}
            for j in range(i,n):
                frequency[s[j]] = frequency.get(s[j],0) + 1
            
                ## Condition => frequency check
                if frequency[s[j]] > 2:
                    break 
                ## maximum length updating
                max_len = max(max_len,j - i + 1)
        return max_len


