from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c : i for i, c in enumerate(s)}
        left, right = 0, 0
        ans = []
        for i, c in enumerate(s):
            right = max(right, last[c])
            if i == right:
                n = right - left + 1
                ans.append(n)
                left = i + 1
        return ans