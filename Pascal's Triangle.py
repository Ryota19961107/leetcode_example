from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        ans = [[1]]
        hold = [0,1,0]
        while len(ans) < numRows:
            row = []
            for i in range(1, len(hold)):
                row.append(hold[i - 1] + hold[i])
            ans.append(row)
            hold = [0] + row + [0]
        return ans