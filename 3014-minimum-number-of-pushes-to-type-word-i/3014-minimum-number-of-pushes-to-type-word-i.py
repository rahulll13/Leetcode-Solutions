class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushcnt = 0
        for i in range(n):
            pushcnt += i // 8 + 1
        return pushcnt