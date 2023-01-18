from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        def backtrace(candidates: List[int], start: int):
            if candidates not in results:
                results.append(list(candidates))
            
            for i in range(start, len(nums)):
                candidates.append(nums[i])
                backtrace(candidates, i + 1)
                candidates.pop()
        
        backtrace([], 0)
        return results