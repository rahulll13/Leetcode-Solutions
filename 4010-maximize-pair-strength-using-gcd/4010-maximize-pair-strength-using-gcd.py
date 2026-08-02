import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        max_strength = 0
        n = len(nums)
        for i in range(n):
            for j in range( i + 1, n):
                curr_gcd = math.gcd(nums[i],nums[j])
                strength = (nums[i] * nums[j]) // (curr_gcd ** 2)
                
                if strength > max_strength:
                     max_strength = strength
        
        return max_strength