from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.sort()
            return
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1] , nums[j] = nums[j], nums[i - 1]
        k =  len(nums) - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1


        
        """
        Do not return anything, modify nums in-place instead.
        """