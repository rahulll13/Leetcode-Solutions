class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2) + [inf]
        def far(a):
            return arr2[bisect_left(arr2, a - d)] > a + d
        return sum(map(far, arr1))