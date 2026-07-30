class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Overwrite the trailing zeros in nums1 with the elements of nums2
        for i in range(n):
            nums1[m + i] = nums2[i]
        # Sort nums1 in-place
        nums1.sort()