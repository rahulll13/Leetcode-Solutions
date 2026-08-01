class Solution:
    def predictTheWinner(self, a: List[int]) -> bool:
        f = cache(lambda i,j:i<j and sum(a[i:j])-min(f(i+1,j),f(i,j-1)))
        return f(0,len(a))>=sum(a)/2