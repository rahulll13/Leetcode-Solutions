class Solution:
    def digitSum(self, s: str, k: int) -> str:
        return len(s)>k and self.digitSum(''.join(str(sum(map(int,q)))
            for q in batched(s,k)),k) or s