import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store intervals along with their original indices with the specific rate
        # Okay now lets run and this this




























        indexed_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            indexed_intervals.append((l, r, w, i))
        
        # Sort intervals by their start times
        indexed_intervals.sort(key=lambda x: x[0])
        n = len(indexed_intervals)
        
        # Precompute the index of the next non-overlapping interval using binary search
        starts = [x[0] for x in indexed_intervals]
        next_idx = []
        for i in range(n):
            # Find the first interval that starts strictly after the current interval ends
            idx = bisect.bisect_right(starts, indexed_intervals[i][1])
            next_idx.append(idx)
            
        # dp[i][j] stores a tuple: (max_weight, sorted_tuple_of_indices)
        # Initialize the DP table with 0 weight and empty index tuples
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        # Process from right to left (suffix DP)
        for i in range(n - 1, -1, -1):
            l, r, w, orig_idx = indexed_intervals[i]
            nxt = next_idx[i]
            
            for j in range(1, 5):
                # Option 1: Skip the current interval
                best_w, best_idx = dp[i + 1][j]
                
                # Option 2: Take the current interval
                take_w, take_sub_idx = dp[nxt][j - 1]
                take_w += w
                
                # Maintain the indices in sorted order for lexicographical comparison
                take_idx = list(take_sub_idx)
                bisect.insort(take_idx, orig_idx)
                take_idx = tuple(take_idx)
                
                # Choose the option with the maximum weight, breaking ties lexicographically
                if take_w > best_w:
                    best_w = take_w
                    best_idx = take_idx
                elif take_w == best_w:
                    if not best_idx or take_idx < best_idx:
                        best_idx = take_idx
                dp[i][j] = (best_w, best_idx)
        # Return the optimal list of indices from the full array with a quota of 4
        return list(dp[0][4][1])