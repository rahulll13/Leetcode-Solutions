class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for X in nums:
            if X in seen:
                return X
            else:
                seen.add(X)