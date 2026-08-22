class Solution:
    def reverse(self, x: int) -> int:
        sign = 1

        if x < 0:
            sign = -1
            x = -x

        res = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if sign == 1 and res * 10 + digit > 2147483647:
                return 0
            elif sign == -1 and res * 10 + digit > 2147483648:
                return 0
            else:
                res = res * 10 + digit

        return res * sign

        