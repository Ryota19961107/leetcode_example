from typing import List

from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) == 1:
            return 0
        
        hashmap = defaultdict(int)
        ans = 0
        for i in range(len(time)):
            surplus = time[i] % 60
            if (60 - surplus) % 60 in hashmap:
                ans += hashmap[(60 - surplus) % 60]
            hashmap[surplus] += 1
        return ans