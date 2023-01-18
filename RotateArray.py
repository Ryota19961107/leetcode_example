from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i + k) % len(nums)] = nums[i]
        nums[:] = a
        """
        Do not return anything, modify nums in-place instead.
        """