class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        freq = Counter(s[:n >> 1]) 
        half = "".join(c * freq[c] for c in ascii_lowercase)
        mid = s[n >> 1] if n & 1 else ""
        return half + mid + half[::-1]