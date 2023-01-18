from typing import List

import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = collections.Counter(nums)
        ans = [i for i in hashmap.keys() if hashmap[i] > len(nums) / 3 ]
        return ans