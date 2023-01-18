from typing import List

import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return True
        hashmap = collections.defaultdict(int)
        for num in arr:
            hashmap[num] += 1
        return len(set(hashmap.values())) == len(hashmap.keys())