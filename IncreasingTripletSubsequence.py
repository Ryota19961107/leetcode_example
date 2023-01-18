from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first_smallest, second_smallest = 2 ** 31, 2 ** 31 
        for n in nums:
            if n <= first_smallest:
                first_smallest = n
            elif n <= second_smallest:
                second_smallest = n
            else:
                return True
        return False