from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min = 9999
        max = -1
        

        for i in range(len(nums)):
            if nums[i] < min:
                min = nums[i]
                max = -1
            if nums[i] > max:
                max = nums[i]
                
        
        result = max - min
        return result
       
                

if __name__ == "__main__":
    sol = Solution()

    nums = [1,1,7,3,7]
    
    sol.maxProfit(nums)
    k = sol.maxProfit(nums)

    
    print( k)