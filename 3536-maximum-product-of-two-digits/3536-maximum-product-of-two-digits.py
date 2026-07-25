class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits.sort()
        return digits[-1] * digits[-2]