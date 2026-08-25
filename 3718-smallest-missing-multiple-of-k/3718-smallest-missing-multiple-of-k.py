class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        smallest = 1
        mul_k = set()
        for num in nums:
            if num % k == 0:
                mul_k.add(num // k)
            if num // k == smallest:
                while smallest in mul_k:
                    smallest += 1
        return smallest * k