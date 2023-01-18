from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L, R = 0, len(nums) - 1
        ans = []
        while R >= L:
            if abs(nums[L]) >= abs(nums[R]):
                ans.append(nums[L] ** 2)
                L += 1
            else:
                ans.append(nums[R] ** 2)
                R -= 1
        ans.reverse()
        return ans