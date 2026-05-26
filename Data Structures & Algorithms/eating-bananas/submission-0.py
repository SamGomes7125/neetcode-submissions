class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        ans = right

        while left <= right:

            mid = (left + right) // 2

            h1 = 0

            for i in range(len(piles)):

                # ceiling division
                h1 += (piles[i] + mid - 1) // mid

            # speed works
            if h1 <= h:

                ans = mid

                # try smaller speed
                right = mid - 1

            # speed too slow
            else:

                left = mid + 1

        return ans