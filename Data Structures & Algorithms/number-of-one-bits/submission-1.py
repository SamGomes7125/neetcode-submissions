class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        h = {}
        for i in range(len(s)):
            if s[i] in h:
                h[s[i]] += 1
            else:
                h[s[i]] = 1
        return bin(n).count("1")

        