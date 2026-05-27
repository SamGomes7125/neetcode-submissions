class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums)-1
        mid = (p1 + p2) // 2
        
        while p1<p2:
            if nums[mid] > nums[p2]:
                p1 = mid + 1 
            else:
                p2 = mid 
            mid = (p1 + p2) // 2
        return nums[mid]


        