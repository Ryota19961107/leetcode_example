from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i == j:
                    continue
                elif isConnected[i][j] == 1:
                    ans += 1
                else:
                    continue
        return ans