from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for k, v in enumerate(nums):
            if v == target and ans == []:
                ans.append(k)
            if v == target and k == len(nums) - 1:
                ans.append(k)
                return ans
            elif v == target and nums[k + 1] != target:
                ans.append(k)
        if len(ans) == 2:
            return ans
        else:
            return [-1, -1]