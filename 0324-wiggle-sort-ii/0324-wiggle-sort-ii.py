class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # Edge case: empty or single-element array
        if len(nums) <= 1:
            return

        # Create a sorted copy
        arr = sorted(nums)

        n = len(nums)

        # Find the middle point
        mid = (n + 1) // 2

        # Reverse the smaller half
        left = arr[:mid][::-1]

        # Reverse the larger half
        right = arr[mid:][::-1]

        # Place elements alternately
        for i in range(mid):
            # Place from smaller half
            nums[2 * i] = left[i]

            # Place from larger half if index exists
            if 2 * i + 1 < n:
                nums[2 * i + 1] = right[i]