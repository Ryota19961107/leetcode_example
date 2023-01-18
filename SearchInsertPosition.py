from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        mid = left + (right - left) //2
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right