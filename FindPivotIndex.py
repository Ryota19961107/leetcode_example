from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        l_sum, r_sum = sum(nums[: i]), sum(nums[i + 1:])
        while i != len(nums):
            if l_sum == r_sum:
                return i
            else:
                i += 1
                l_sum, r_sum = sum(nums[: i]), sum(nums[i + 1:])
        return -1