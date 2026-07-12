class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        rank = {}  ## making a Set for storing the rank of the arr elements
        current_rank = 1
        for num in sorted_arr:
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1
        return [rank[num] for num in arr]