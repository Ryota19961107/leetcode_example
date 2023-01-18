from typing import List

class solutions:
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) > len(nums) // 2:
                return i
            else:
                continue