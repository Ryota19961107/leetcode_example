from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrace(remain: int, comb: List[int], start: int):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrace(remain-candidates[i], comb, i)
                comb.pop()
            
        backtrace(remain=target, comb=[], start=0)

        return results