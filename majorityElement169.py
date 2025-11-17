from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        n = -1

        for i in range(len(nums)):
            if count == 0 and n != nums[i]:
                count =+ 1
                n = nums[i]
            if count != 0 and n == nums[i]:
                count +=1
            if count != 0 and n != nums[i]:
                count -=1

        return n


#NAIVE SOLUTION
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         #[3,2,3]
#         count = {}
#         for i in nums:
#             if i in count:
#                 count[i] += 1
#             else:
#                 count[i] = 1
        
#         print(count)

#         maxCount = -1
#         result = -1
        
        
#         for key, val in count.items():
#             if maxCount < val:
#                 maxCount = val
#                 result = key
        
#         return result Time: O(n) Space: O(n)
        

if __name__ == "__main__":
    sol = Solution()

    nums = [3,2,3,2,2,2,1,1,1,1]
    
    sol.majorityElement(nums)
    k = sol.majorityElement(nums)

    
    print( k)