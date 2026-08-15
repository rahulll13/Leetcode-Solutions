class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if not nums:
            return 0
        xor_value = 0
        has_non_zero = False

        for num in nums:
            xor_value ^= num

            if num != 0:
                has_non_zero = True
        if xor_value  != 0:
            return len(nums)
        
        if not has_non_zero:
            return 0
        
        return len(nums) - 1