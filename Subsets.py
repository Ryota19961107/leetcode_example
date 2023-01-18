from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrace(comb: List[int], start: int):
            results.append(list(comb))
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrace(comb, i + 1)
                comb.pop()
        
        backtrace([], 0)
        return results