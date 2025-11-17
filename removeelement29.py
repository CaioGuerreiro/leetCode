from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

if __name__ == "__main__":
    sol = Solution()

    nums = [3,2 ,1, 421, 2, 3, 45,3,1]
    val = 3

    k = sol.removeElement(nums, val)

    print("k =", k)
    print("nums após remover val:", nums[:k])