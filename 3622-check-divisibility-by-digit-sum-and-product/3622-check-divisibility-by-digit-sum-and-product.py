class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        sum = 0
        prod = 1
        while num != 0:
            digits = num % 10
            sum += digits
            prod *= digits
            num //= 10
        divisor = sum + prod
        if n % divisor == 0:
            return True
        else:
            return False