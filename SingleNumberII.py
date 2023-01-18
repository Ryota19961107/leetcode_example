from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)-1, 3):
            if nums[i] != nums[i - 1] and nums[i] == nums[i + 1]:
                return nums[i - 1]
        return nums[-1]