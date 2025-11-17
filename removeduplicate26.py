from typing import List

#remove duplicates numbers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        
        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
               nums[l] = nums[i]
               l+=1
        return l
                
            



if __name__ == "__main__":
    sol = Solution()

    nums = [0,0,1,1,1,2,2,3,3,4,5,6,7]

    k = sol.removeDuplicates(nums)
    print("k =", k)
    print( nums[:k])
