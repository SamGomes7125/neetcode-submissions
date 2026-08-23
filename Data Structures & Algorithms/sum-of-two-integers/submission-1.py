class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
        if a > 2**31 - 1:
            a = a - 2**32
        return a

        