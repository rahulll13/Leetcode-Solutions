class Solution:
    def elevatorRequests(self, n: int, requests: List[int]) -> int:
        ans = requests[0]

        for i in range(1, len(requests)):
            ans += abs(requests[i] - requests[i - 1])

        return ans