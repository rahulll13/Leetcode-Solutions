class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        MAXX = 2048

        pair = [False] * MAXX
        triplet = [False] * MAXX

        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                pair[nums[i] ^ nums[j]] = True

        for x in range(MAXX):

            if not pair[x]:
                continue

            for v in nums:
                triplet[x ^ v] = True

        return sum(triplet)