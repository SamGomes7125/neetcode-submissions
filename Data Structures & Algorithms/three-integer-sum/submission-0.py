class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        l = len(nums)
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            d1 = 0 - nums[i]
            j = i+1
            k = l-1
            while j<k:
                if nums[j]+nums[k]<d1:
                    j = j+1
                elif nums[j]+nums[k]>d1:
                    k = k-1
                elif nums[j]+nums[k]==d1:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return result

                
        
        