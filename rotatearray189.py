from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # empurrar os numeros dentro do array
        k = k % len(nums) # k não pode ser maior que o array
        l = 0
        r = len(nums) - 1
        # [7,6,5,4,3,2,1]
        #        l
        #        r
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
        l = 0
        r = k -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
        l = k
        r = len(nums) -1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        

if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,3,4,5,6,7]
    val = 3

    k = sol.rotate(nums, val)

    print("k =", k)
    print( nums)