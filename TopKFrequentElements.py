from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        memo = collections.Counter(nums)
        return heapq.nlargest(k, memo.keys(), key=memo.get)      