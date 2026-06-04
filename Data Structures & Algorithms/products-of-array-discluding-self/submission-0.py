class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_product = 1
        for i in range(len(nums)):
            tot_product = tot_product*nums[i]
        zero_count = nums.count(0)
        result = []
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            product = 1
            for n in nums:
                if n != 0:
                    product *= n
            result = []

            for n in nums:
                if n == 0:
                    result.append(product)
                else:
                    result.append(0)    
        else:
            for i in range(len(nums)):
                    result.append(int(tot_product/nums[i]))

        return result
        