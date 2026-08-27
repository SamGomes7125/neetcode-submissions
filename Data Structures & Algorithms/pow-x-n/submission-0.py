class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        base = x
        while n > 0:
            if n % 2 == 1:
                res = res * base

            base = base * base
            n = n // 2

        return res
        