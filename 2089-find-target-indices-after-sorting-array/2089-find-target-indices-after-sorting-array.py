from bisect import bisect_left, bisect_right
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        left = bisect_left(nums,target)
        right = bisect_right(nums,target)
        return list(range(left,right))
