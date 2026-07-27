class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorrt = nums.sort()

        canditate_1 = nums[-1] - 1
        candiate_2 = nums[-2] - 1

        return canditate_1 * candiate_2
