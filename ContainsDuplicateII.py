from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, kv in enumerate(nums):
            if kv in d:
                if i - d[kv] <= k:
                    return True
            d[kv] = i
        return False