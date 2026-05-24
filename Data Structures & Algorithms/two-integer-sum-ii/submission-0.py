class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        l = len(numbers)
        j=l-1
        while i<j:  
            if numbers[i]+numbers[j]>target:
                j=j-1
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                return [i+1,j+1]
            
                
        
        