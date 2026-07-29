class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 

        total_sum = sum(nums)
        expected_sum = (n * (n + 1)) // 2

        ans = expected_sum - total_sum

        return ans