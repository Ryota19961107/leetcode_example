from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain: int, comb: List[int], start: int):
            if len(comb) == k and remain == 0:
                results.append(list(comb))
                return
            elif len(comb) == k and remain != 0:
                return
            
            for i in range(start, 10):
                comb.append(i)
                backtrack(remain - i, comb, i + 1)
                comb.pop()
        backtrack(remain=n, comb=[], start=1)
        return results