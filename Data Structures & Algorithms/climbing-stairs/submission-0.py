class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {}
        for i in range(n+1):
            if i-2 in ways:
                ways[i] = ways.get(i-1)+ways.get(i-2)
            elif i-1 in ways and i-2 not in ways:
                ways[i] = ways.get(i-1)
            else:
                ways[i] = 1
        return ways[n]



        