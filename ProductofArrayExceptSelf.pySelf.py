from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce
        from operator import mul

        ans = [None] * len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
        R = 1
        for i in reversed(range(len(nums))):
            ans[i] *= R
            R *= nums[i]
        return ans