# we can solve this with brute force
# parsing element by element and compare them
# the time complexity will be O(n^2), but space complexity is O(1)
# another approach is sorting the array, this will reduce the time
# complexity for O(n logn) and space complexity is O(1)
# another approach is creating a hashset, the time complexity will be
# O(n), but the space complexity will be O(n)


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



def mergeSort(nums):
  if len(nums) <= 1:
    return nums

  mid = len(nums) // 2
  leftHalf = nums[:mid]
  rightHalf = nums[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

            


if __name__ == "__main__":
    sol = Solution()

    nums=[1,2,3,1,2,3]
    

    #l = sol.hasDuplicate(nums)

    #print(l)
    print(nums)
    sortList = mergeSort(nums)
    print(sortList)

    






